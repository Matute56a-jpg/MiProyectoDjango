from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    msgs = Message.objects.filter(recipient=request.user).order_by("-created_at")
    return render(request, "messenger/inbox.html", {"messages_list": msgs})

@login_required
def sent(request):
    msgs = Message.objects.filter(sender=request.user).order_by("-created_at")
    return render(request, "messenger/sent.html", {"messages_list": msgs})

@login_required
def compose(request, reply_to_id=None):
    initial = {}
    if reply_to_id:
        original = get_object_or_404(
            Message,
            Q(id=reply_to_id) & (Q(recipient=request.user) | Q(sender=request.user))
        )
        initial = {
            "recipient": original.sender if original.recipient == request.user else original.recipient,
            "subject": f"Re: {original.subject}",
        }

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, "Mensaje enviado.")
            return redirect("messenger_sent")
    else:
        form = MessageForm(initial=initial)

    return render(request, "messenger/compose.html", {"form": form})

@login_required
def detail(request, pk):
    msg = get_object_or_404(
        Message,
        Q(id=pk) & (Q(recipient=request.user) | Q(sender=request.user))
    )
    if msg.recipient == request.user and not msg.read:
        msg.read = True
        msg.save(update_fields=["read"])
    return render(request, "messenger/detail.html", {"message": msg})
