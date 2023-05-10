from django.db import models
from django.utils.translation import gettext as _


class Imagine(models.Model):
    nume = models.CharField(max_length=100, verbose_name=_('Nume Imagine'))
    imagine = models.ImageField(upload_to='galerie/')
    data_creare = models.DateTimeField(auto_now_add=True, verbose_name=_('Data creare'))

    def __str__(self):
        return str(self.nume)

    class Meta:
        ordering = ["-data_creare"]
        verbose_name_plural = _("Imagini")
