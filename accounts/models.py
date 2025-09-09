from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_avatar_path(instance, filename):
    return f"avatars/{instance.user.username}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField("Nombre", max_length=150, blank=True)
    last_name = models.CharField("Apellido", max_length=150, blank=True)
    bio = models.TextField("Biografía", blank=True)
    avatar = models.ImageField("Avatar", upload_to=user_avatar_path, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()
