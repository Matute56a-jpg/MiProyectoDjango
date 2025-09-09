from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_object_or_404
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
@login_required
def compose(request, reply_to_id=None):
    initial = {}
    # Si viene reply_to_id, precargar destinatario y subject
    if reply_to_id:
        original = get_object_or_404(
            Message,
            pk=reply_to_id,
            queryset=Message.objects.filter(
                models.Q(sender=request.user) | models.Q(recipient=request.user)
            )
        )
        destinatario = original.recipient if original.sender == request.user else original.sender
        subj = original.subject or ''
        initial.update({
            "recipient": destinatario,
            "subject": (f"Re: {subj}" if not subj.lower().startswith("re:") else subj),
            "in_reply_to": original,
        })

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            # Si el form no trae in_reply_to pero estamos respondiendo, setearlo
            if reply_to_id and not msg.in_reply_to_id:
                msg.in_reply_to_id = reply_to_id
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

