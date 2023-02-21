from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("search/", views.search, name="search"),
    path('useri/', include('useri.urls')),
    path('parcare/', include('parcare.urls')),
    path('staff/', include('staff.urls')),
    path('clienti/', include('clienti.urls')),
    path('plati/', include('plati.urls')),
    path('', views.main, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)