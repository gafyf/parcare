from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

def user_directory_path(instance, filename):
    return "users_images/{profil}/{filen}.jpg".format(profil=instance.prenume, file=filename, filen=instance.prenume)

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nume = models.CharField(max_length=100, blank=True, null=True)
    prenume = models.CharField(max_length=100, blank=True, null=True)
    cnp = models.CharField(max_length=20, blank=True, null=True)
    judet = models.CharField(max_length=20, blank=True, null=True)
    oras = models.CharField(max_length=20, blank=True, null=True)
    adresa = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    imagine = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    data_creare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.prenume)

    def get_absolute_url(self):
        return reverse("useri:profil_edit", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Profile"
        ordering = ["-data_creare"]       
