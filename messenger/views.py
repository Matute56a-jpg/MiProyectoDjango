from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    msgs = (Message.objects
            .select_related('sender','recipient')
            .filter(recipient=request.user)
            .order_by('-created_at'))
    return render(request, 'messenger/inbox.html', {'messages_list': msgs})

@login_required
def sent(request):
    msgs = (Message.objects
            .select_related('sender','recipient')
            .filter(sender=request.user)
            .order_by('-created_at'))
    return render(request, 'messenger/sent.html', {'messages_list': msgs})

@login_required
def detail(request, pk):
    # ✅ CORRECTO: pasamos el QuerySet como primer argumento a get_object_or_404
    qs = (Message.objects
          .select_related('sender','recipient')
          .filter(models.Q(sender=request.user) | models.Q(recipient=request.user)))
    msg = get_object_or_404(qs, pk=pk)

    # marcar leído si soy destinatario
    if msg.recipient_id == request.user.id and not msg.read:
        msg.read = True
        msg.save(update_fields=['read'])

    # cargar hilo de respuestas (opcional, si quieres mostrar la charla)
    thread = (Message.objects
              .select_related('sender','recipient')
              .filter(models.Q(pk=msg.pk) | models.Q(in_reply_to=msg))
              .order_by('created_at'))

    return render(request, 'messenger/detail.html', {'message': msg, 'thread': thread})

@login_required
def compose(request, reply_to_id=None):
    initial = {}
    original = None

    if reply_to_id:
        # ✅ CORRECTO: QuerySet como primer argumento
        qs = Message.objects.filter(
            models.Q(sender=request.user) | models.Q(recipient=request.user)
        )
        original = get_object_or_404(qs, pk=reply_to_id)

        destinatario = original.recipient if original.sender == request.user else original.sender
        subj = original.subject or ''
        initial.update({
            'recipient': destinatario,
            'subject': (f'Re: {subj}' if not subj.lower().startswith('re:') else subj),
        })

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            if original and reply_to_id:
                msg.in_reply_to = original
            msg.save()
            messages.success(request, 'Mensaje enviado ✅')
            return redirect('messenger_sent')
        else:
            # para ver los errores en la consola
            print('ERRORES FORM compose:', form.errors.as_json())
            messages.error(request, 'Revisá el formulario.')
    else:
        form = MessageForm(initial=initial)

    return render(request, 'messenger/compose.html', {'form': form, 'original': original})
