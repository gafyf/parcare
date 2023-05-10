from django.db import models
from useri.models import Profil
import uuid
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


TIP_FUNCTIE = (
        (None, _('Selecteaza functie')),
        ('paznic', _('paznic')),
        ('electrician', _('electrician')),
        ('casier', _('casier')),
        ('secretara', _('secretara')),
        ('director', _('director'))
    )

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, blank=True, null=True)
    functie = models.CharField(max_length=50, choices=TIP_FUNCTIE, blank=True, null=True, verbose_name=_('Functie'))
    data_angajarii = models.DateTimeField(auto_now_add=True, verbose_name=_('Data angajarii'))
    pdf = models.FileField(upload_to='contracte_staff/', blank=True, null=True)
    numar = models.PositiveIntegerField(default=0, verbose_name=_('Nr Angajat'))


    def __str__(self):
        return f"{self.numar} - {self.functie} - {self.profil}"

    def get_absolute_url(self):
        return reverse("useri:profil_edit", args=[str(self.profil.id)])
    
    def get_contract_url(self):
        return reverse("staff:staff_contract", args=[str(self.profil.id)])

    class Meta:
        verbose_name_plural = _("Angajati")
        ordering = ["-data_angajarii"]   
