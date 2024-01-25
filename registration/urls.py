from django.urls import path,include
from .views import Registro
urlpatterns = [
path('registro',Registro.as_view(),name='registro'),
]