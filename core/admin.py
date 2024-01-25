from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Competicion, Equipos, Jugador

# Register your models here.

class CompeticionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lugar', 'fechaCreacion')
    list_filter = ('nombre', 'lugar', 'fechaCreacion')
    search_fields = ('nombre', 'lugar', 'fechaCreacion')
    date_hierarchy = 'fechaCreacion'

admin.site.register(Competicion, CompeticionAdmin)

class EquiposAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'responsable')
    list_filter = ('nombre', 'categoria', 'responsable')
    search_fields = ('nombre', 'categoria', 'responsable')
    date_hierarchy = 'fechaCreacion'

admin.site.register(Equipos, EquiposAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'edad','equipo')
    list_filter = ('nombre', 'correo', 'edad','equipo')
    search_fields = ('nombre', 'correo', 'edad','equipo')
    date_hierarchy = 'fechaCreacion'

admin.site.register(Jugador, JugadorAdmin)
