from django.urls import path
from . import views

app_name = 'parcare'
urlpatterns = [
    path('', views.parcare, name='parcare'),
    path('tarife/', views.tarife, name='tarife'),
    path('tarife_ora/', views.tarife_ora, name='tarife_ora'),
    path('abonamente/', views.abonamente, name='abonamente'),
    path('carduri/', views.carduri, name='carduri'),
    path('info_client_contract_pdf/', views.info_client_contract_pdf, name='info_client_contract_pdf'),
    path('termeni_si_conditii/', views.termeni_si_conditii, name='termeni_si_conditii'),
    path('servicii/', views.servicii, name='servicii'),
    path('contact/', views.contact, name='contact'),
    path('galerie/', views.galerie, name='galerie')
]