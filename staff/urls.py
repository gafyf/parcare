from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('staff_nou/<str:pk>/', views.staff_nou, name='staff_nou'),
    path('masina_noua/<str:pk>/', views.masina_noua, name='masina_noua'),
    path('contract/', views.contract, name='contract'),
    path('staff_contract/<str:pk>/', views.staff_contract, name='staff_contract')
]