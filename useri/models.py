from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.utils.translation import gettext as _

def user_directory_path(instance, filename):
    return "users_images/{profil}/{filen}.jpg".format(profil=instance.prenume, file=filename, filen=instance.prenume)

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('User'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nume = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Nume'))
    prenume = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Prenume'))
    cnp = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('CNP'))
    judet = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Judet'))
    oras = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Oras'))
    adresa = models.CharField(max_length=1000, blank=True, null=True, verbose_name=_('Adresa'))
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Telefon'))
    imagine = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name=_('Imagine'))
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))

    def __str__(self):
        return str(self.prenume)

    def get_absolute_url(self):
        return reverse("useri:profil_edit", args=[str(self.id)])

    class Meta:
        verbose_name_plural = _("Profile")
        ordering = ["-data_creare"]       
