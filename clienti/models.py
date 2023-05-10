import uuid
from django.db import models
from useri.models import Profil
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, blank=True, null=True)
    nr_permis = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Nr permis'))
    categ_permis = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Ctg permis'))
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))

    def __str__(self):
        return f"{self.profil} -  {self.data_creare}"

    class Meta:
        verbose_name_plural = _("Clienti")
        ordering = ["-data_creare"]   


TIP = (
        (None, _('Selecteaza contract')),
        ('public', _('Public (500 Lei)')),
        ('privat', _('Privat (800 Lei)')),
    )

class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name=_('contracts'), blank=True, null=True)
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))
    data_expirare = models.DateTimeField(default=timezone.now, verbose_name=_('Data expirare'))
    platit = models.BooleanField(default=False, verbose_name=_('Platit'))
    contract = models.CharField(max_length=50, choices=TIP, blank=True, verbose_name=_('Contract'))
    numar = models.PositiveIntegerField(default=0, verbose_name=_('Numar'))
    pdf = models.FileField(upload_to='contracte_clienti/', blank=True, null=True)
    


    def __str__(self):
        return f"{self.numar} -  {self.profil}" 

    def get_absolute_url(self):
        return reverse("clienti:contract_pdf", args=[str(self.id)])
    
    def has_expired(self):
        if self.platit and self.data_expirare.date() < timezone.now().date():
            self.platit = False
            self.save()
    
    class Meta:
        verbose_name_plural = _("Contracte")
        ordering = ["-data_creare"]   


class Masina(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ManyToManyField(Profil, related_name=_('Masini'))
    p_json = models.JSONField(default=dict, blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Marca'))
    model = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Model'))
    numar = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Numar'))
    culoare = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Culoare'))
    combustibil = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Combustibil'))
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))

    def __str__(self):
        return str(self.numar)

    def get_absolute_url(self):
        return reverse("clienti:masina", args=[self.id])

    class Meta:
        verbose_name_plural = _("Masini")
        ordering = ["-data_creare"]
