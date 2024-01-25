from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'),
    path('listado/', views.listadoEquipos.as_view(), name='listado'),
    path('crear/',views.crearEquipos.as_view(), name='crear'),
    path('borrar/<int:pk>', views.borrarEquipos.as_view(), name='borrar'),
    path('modificar/<int:pk>', views.modificarEquipos.as_view(), name='modificar'),

    path('listadoJugador/', views.listadoJugador.as_view(), name='listadoJugador'),
    path('crearJugador/',views.crearJugador.as_view(), name='crearJugador'),
    path('borrarJugador/<int:pk>', views.borrarJugador.as_view(), name='borrarJugador'),
    path('modificarJugador/<int:pk>', views.modificarJugador.as_view(), name='modificarJugador'),

    path('listadoCompeticion/', views.listadoCompeticion.as_view(), name='listadoCompeticion'),
    path('crearCompeticion/',views.crearCompeticion.as_view(), name='crearCompeticion'),
    path('borrarCompeticion/<int:pk>', views.borrarCompeticion.as_view(), name='borrarCompeticion'),
    path('modificarCompeticion/<int:pk>', views.modificarCompeticion.as_view(), name='modificarCompeticion'),

    path('jugadorDetalle/<int:pk>',views.jugadorDetalle.as_view(),name='jugadorDetalle'),
    path('competicionDetalla/<int:pk>',views.competicionDetalle.as_view(),name='competicionDetalle'),
    path('equiposDetalle/<int:pk>',views.equiposDetalle.as_view(),name='equiposDetalle'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)