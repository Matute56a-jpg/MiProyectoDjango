from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=150, required=False)
    last_name  = forms.CharField(label='Apellido', max_length=150, required=False)
    email      = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
