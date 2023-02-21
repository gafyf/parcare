from django.urls import path
from . import views
from . import pdf

app_name = 'plati'

urlpatterns = [
    path('<str:pk>', views.plati, name='plati'),
    path('factura_client_pdf/', pdf.factura_client_pdf, name='factura_client_pdf'),
    path('facturi/<str:pk>', views.facturi, name='facturi'),
    path('factura_pdf/<str:pk>', views.factura_pdf, name='factura_pdf'),
    path('email_plata', views.email_plata, name='email_plata'),
]