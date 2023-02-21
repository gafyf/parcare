from django.db import models


class Imagine(models.Model):
    nume = models.CharField(max_length=100)
    imagine = models.ImageField(upload_to='galerie/')
    data_creare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nume)

    class Meta:
        ordering = ["-data_creare"]
        verbose_name_plural = "Imagini"

