from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), #para el login
    path('accounts/', include('registration.urls')), #para el login
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]