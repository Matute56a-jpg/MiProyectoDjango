from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile

@login_required
def profile(request):
    profile = getattr(request.user, "profile", None)
    if profile is None:
        profile = Profile.objects.create(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile})

@login_required
def profile_edit(request):
    profile = getattr(request.user, "profile", None)
    if profile is None:
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, "accounts/profile_edit.html", {"form": form})
