from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "bio", "avatar"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["first_name"].initial = self.user.first_name
        self.fields["last_name"].initial = self.user.last_name
        self.fields["email"].initial = self.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        self.user.first_name = self.cleaned_data.get("first_name", self.user.first_name)
        self.user.last_name = self.cleaned_data.get("last_name", self.user.last_name)
        self.user.email = self.cleaned_data.get("email", self.user.email)
        if commit:
            self.user.save()
            profile.user = self.user
            profile.save()
        return profile
