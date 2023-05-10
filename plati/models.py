from django.db import models
from useri.models import Profil
import uuid
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Card(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name=_('Posesor Card'))
    card_number = models.CharField(max_length=16, blank=False, null=False, verbose_name=_('Numar Card'))
    expiration_month = models.CharField(max_length=2, blank=False, null=False, verbose_name=_('Luna Expirare'))
    expiration_year = models.CharField(max_length=2, blank=False, null=False, verbose_name=_('An Expirare'))
    cvc = models.CharField(max_length=3, blank=False, null=False, verbose_name=_('CVC'))

    def __str__(self):
        return f"{self.name} - **** **** **** {self.card_number[-4:]}"

class Factura(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))
    numar = models.PositiveIntegerField(default=0, verbose_name=_('Numar'))
    pdf = models.FileField(upload_to='facturi/', blank=True, null=True)


    def __str__(self):
        return f"{self.numar} -  {self.profil}"
    
    def get_absolute_url(self):
        return reverse("plati:factura_pdf", args=[str(self.id)])

    class Meta:
        ordering = ["-data_creare"]
        verbose_name_plural = _("Facturi")