from django import forms
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        label='Para'
    )

    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
