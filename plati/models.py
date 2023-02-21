from django.db import models
from useri.models import Profil
import uuid
from django.urls import reverse


class Card(models.Model):
    name = models.CharField(max_length=100, default='')
    card_number = models.CharField(max_length=16, blank=False, null=False)
    expiration_month = models.CharField(max_length=2, blank=False, null=False)
    expiration_year = models.CharField(max_length=2, blank=False, null=False)
    cvc = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return f"{self.name} - **** **** **** {self.card_number[-4:]}"

class Factura(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_creare = models.DateTimeField(auto_now_add=True)
    numar = models.PositiveIntegerField(default=0)
    pdf = models.FileField(upload_to='facturi/', blank=True, null=True)


    def __str__(self):
        return f"{self.numar} -  {self.profil}"
    
    def get_absolute_url(self):
        return reverse("plati:factura_pdf", args=[str(self.id)])

    class Meta:
        ordering = ["-data_creare"]
        verbose_name_plural = "Facturi"