from django.urls import path, include
from . import views


app_name = 'useri'
urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("activate/<str:uidb64>/<str:token>/", views.activate, name="activate"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_reset_form/", views.PasswordResetView.as_view(), name="password_reset_form"),
    path("reset/<str:uidb64>/<str:token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset_done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_reset_complete/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path('profil_edit/<str:pk>/', views.ProfilUpdateView.as_view(), name='profil_edit'),
    path('user_edit/<str:pk>/', views.UserUpdateView.as_view(), name='user_edit'),
    path('delete_user/<str:pk>/', views.DeleteUser.as_view(), name='delete_user'),
    path('delete_profil/<str:pk>/', views.delete_profil, name='delete_profil'),
    path('detalii_profil/<str:pk>/', views.detalii_profil, name='detalii_profil'),
    path('', include("django.contrib.auth.urls")),
]
