import uuid
from django.db import models
from useri.models import Profil
from django.utils import timezone
from django.urls import reverse


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, blank=True, null=True)
    nr_permis = models.CharField(max_length=20, blank=True, null=True)
    categ_permis = models.CharField(max_length=20, blank=True, null=True)
    data_creare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profil} -  {self.data_creare}"

    class Meta:
        verbose_name_plural = "Clienti"
        ordering = ["-data_creare"]   


TIP = (
        (None, 'Selecteaza contract'),
        ('public', 'public'),
        ('privat', 'privat')
    )
class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='contracts', blank=True, null=True)
    data_creare = models.DateTimeField(auto_now_add=True)
    data_expirare = models.DateTimeField(default=timezone.now)
    platit = models.BooleanField(default=False)
    contract = models.CharField(max_length=50, choices=TIP, blank=True)
    numar = models.PositiveIntegerField(default=0)
    pdf = models.FileField(upload_to='contracte_clienti/', blank=True, null=True)
    


    def __str__(self):
        return f"{self.numar} -  {self.profil}" 

    def get_absolute_url(self):
        return reverse("clienti:contract_pdf", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Contracte"
        ordering = ["-data_creare"]   


class Masina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ManyToManyField(Profil, related_name='masini')
    p_json = models.JSONField(default=dict, blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    numar = models.CharField(max_length=20, blank=True, null=True)
    culoare = models.CharField(max_length=20, blank=True, null=True)
    combustibil = models.CharField(max_length=20, blank=True, null=True)
    data_creare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.numar)

    def get_absolute_url(self):
        return reverse("clienti:masina", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Masini"
        ordering = ["-data_creare"]
