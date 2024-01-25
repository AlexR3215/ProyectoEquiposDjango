from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Equipos, Competicion, Jugador
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

class inicio (TemplateView):
    template_name='core/index.html'

class listadoEquipos (ListView):
    model = Equipos

@method_decorator(login_required, name='dispatch') #da error si intentas entrar a crear a traves de la url sin estar logado
class crearEquipos(CreateView):
    model = Equipos
    fields = ['nombre','categoria','competicion','fechaCreacion','foto']
    success_url = reverse_lazy('listado')

    def form_valid(self, form): #validador de datos del usuario
        form.instance.responsable = self.request.user #el usuario que esta identificado en el admin es el que crea el articulo por defecto
        return super(crearEquipos,self).form_valid(form)

@method_decorator(login_required, name='dispatch') #lo mismo que con crear pero con borrar
class borrarEquipos(DeleteView):
    model = Equipos
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        equipo = self.get_object() #me devuelve el articulo que se quiere modificar
        if equipo.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class modificarEquipos(UpdateView):
    model = Equipos
    fields = ['nombre','categoria','competicion','fechaCreacion']
    template_name_suffix = "_update_form"
    success_url =reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        equipo = self.get_object() #me devuelve el articulo que se quiere modificar
        if equipo.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)


########################################################################################################################
    
class listadoJugador (ListView):
    model = Jugador

@method_decorator(login_required, name='dispatch') #da error si intentas entrar a crear a traves de la url sin estar logado
class crearJugador(CreateView):
    model = Jugador
    fields = ['nombre','correo','edad','foto','equipo','fechaCreacion','fechaModificacion']
    success_url = reverse_lazy('listadoJugador')

    def form_valid(self, form): #validador de datos del usuario
        form.instance.responsable = self.request.user #el usuario que esta identificado en el admin es el que crea el articulo por defecto
        return super(crearJugador,self).form_valid(form)

@method_decorator(login_required, name='dispatch') #lo mismo que con crear pero con borrar
class borrarJugador(DeleteView):
    model = Jugador
    success_url = reverse_lazy('listadoJugador')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        jugador = self.get_object() #me devuelve el articulo que se quiere modificar
        if jugador.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class modificarJugador(UpdateView):
    model = Jugador
    fields = ['nombre','correo','edad','foto','equipo','fechaCreacion','fechaModificacion']
    template_name_suffix = "_update_form"
    success_url =reverse_lazy('listadoJugador')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        jugador = self.get_object() #me devuelve el articulo que se quiere modificar
        if jugador.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)

#########################################################################################################################
    
class listadoCompeticion (ListView):
    model = Competicion

@method_decorator(login_required, name='dispatch') #da error si intentas entrar a crear a traves de la url sin estar logado
class crearCompeticion(CreateView):
    model = Competicion
    fields = ['nombre','lugar','foto','fechaCreacion','fechaModificacion']
    success_url = reverse_lazy('listadoCompeticion')

    def form_valid(self, form): #validador de datos del usuario
        form.instance.responsable = self.request.user #el usuario que esta identificado en el admin es el que crea el articulo por defecto
        return super(crearCompeticion,self).form_valid(form)

@method_decorator(login_required, name='dispatch') #lo mismo que con crear pero con borrar
class borrarCompeticion(DeleteView):
    model = Competicion
    success_url = reverse_lazy('listadoCompeticion')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        competicion = self.get_object() #me devuelve el articulo que se quiere modificar
        if competicion.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class modificarCompeticion(UpdateView):
    model = Competicion
    fields = ['nombre','lugar','foto','fechaCreacion','fechaModificacion']
    template_name_suffix = "_update_form"
    success_url =reverse_lazy('listadoCompeticion')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        competicion = self.get_object() #me devuelve el articulo que se quiere modificar
        if competicion.responsable != request.user: #comprobar si el autor es el mismo que el user logeado
            raise PermissionDenied #lanzar un error de permisos
        return super().dispatch(request, *args, **kwargs)


class jugadorDetalle(DetailView):
    model = Jugador

class competicionDetalle(DetailView):
    model = Competicion

class equiposDetalle(DetailView):
    model=Equipos