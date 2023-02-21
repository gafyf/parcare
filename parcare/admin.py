from django.contrib import admin

# Register your models here.

from useri.models import Profil
from clienti.models import Client, Masina , Contract
from staff.models import Staff
from parcare.models import Imagine
from plati.models import Card, Factura


admin.site.register(Profil)
admin.site.register(Client)
admin.site.register(Masina)
admin.site.register(Contract) 
admin.site.register(Staff)
admin.site.register(Imagine)
admin.site.register(Card)
admin.site.register(Factura)

# @admin.register(Profil)
# class ProfilAdmin(admin.ModelAdmin):
#     ordering = ['-data_creare']
