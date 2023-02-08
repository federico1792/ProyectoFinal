from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name='Telefono')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'