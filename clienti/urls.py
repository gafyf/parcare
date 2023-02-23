from django.urls import path
from .views import masina, del_masina, client_nou, contract_pdf, contract_pdf_view

app_name = 'clienti'
urlpatterns = [
    path('masina/<str:pk>/masina/<str:masina_id>/', masina, name='masina'),
    path('del_masina/<str:pk>/delete-masina/<str:masina_id>/', del_masina, name='del_masina'),
    path('contract_pdf/<str:pk>/', contract_pdf, name='contract_pdf'),
    path('client_nou/<str:pk>/', client_nou, name='client_nou'),
    path('contract_pdf_view/', contract_pdf_view, name='contract_pdf_view'),

]
