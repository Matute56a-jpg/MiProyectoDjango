from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Aseguramos que nombre/apellido/email queden guardados
            user.first_name = form.cleaned_data.get('first_name', '')
            user.last_name  = form.cleaned_data.get('last_name', '')
            user.email      = form.cleaned_data.get('email', '')
            user.save()
            messages.success(request, 'Tu cuenta fue creada. ¡Ahora podés iniciar sesión!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    profile = getattr(request.user, "profile", None)
    return render(request, "accounts/profile.html", {"profile": profile})

@login_required
def profile_edit(request):
    profile = getattr(request.user, "profile", None)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_edit.html", {"form": form})
