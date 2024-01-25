from django.db import models

# Create your models here.

from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Competicion(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre de la competición',blank=False, null=False)
    lugar = models.CharField(max_length=30, verbose_name='Lugar de la competición')
    fechaCreacion = models.DateField(default=date.today,blank=False, null=False, verbose_name='fecha de creacion')
    fechaModificacion = models.DateField(default=date.today,blank=False, null=False, verbose_name='fecha de modificacion')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to="imgCompeticion")
    def __str__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Competicion"
    
class Equipos(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del equipo',blank=False, null=False)
    categoria = models.CharField(max_length=30, verbose_name='Nombre de la categoría',blank=False, null=False)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    competicion = models.ManyToManyField(Competicion, verbose_name='Competicion')
    foto = models.ImageField(null=True, blank=True, upload_to="imgEquipo")
    fechaCreacion = models.DateField(default=date.today, blank=False, null=False, verbose_name='fecha de creacion')
    fechaModificacion = models.DateField(default=date.today,blank=False, null=False, verbose_name='fecha de modificacion')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Equipos"

class Jugador(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del Jugador',blank=False, null=False)
    correo = models.EmailField(verbose_name='Correo Electronico')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    foto = models.ImageField(null=True, blank=True, upload_to="imgJugador")
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    fechaCreacion = models.DateField(default=date.today,blank=False, null=False, verbose_name='fecha de creacion')
    fechaModificacion = models.DateField(default=date.today,blank=False, null=False, verbose_name='fecha de modificacion')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Jugadores"