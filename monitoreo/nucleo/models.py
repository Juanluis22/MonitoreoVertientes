from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.

class comunidad(models.Model):
    nombre=models.CharField(max_length=150,verbose_name='Nombre')
    vertientes=models.PositiveIntegerField(default=0)
    ubicación=models.CharField(max_length=200,verbose_name='Ubicación')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='Comunidad'
        verbose_name_plural='Comunidades'
        db_table='comunidad'
        ordering=['id']


class vertiente(models.Model):
    nombre=models.CharField(max_length=150,verbose_name='Nombre')
    desc=models.CharField(max_length=250,verbose_name='Descripcion')
    ubicación=models.CharField(max_length=200,verbose_name='Ubicación')
    comunidad=models.ForeignKey(comunidad, on_delete=models.SET_NULL, null=True)

    caudal=models.IntegerField(default=0)
    pH=models.IntegerField(default=0)
    conductividad=models.IntegerField(default=0)
    turbiedad=models.IntegerField(default=0)
    temperatura=models.IntegerField(default=0)
    humedad=models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='Vertiente'
        verbose_name_plural='Vertientes'
        db_table='vertiente'
        ordering=['id']


class habitantes(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE,unique=True)

    nombre=models.CharField(max_length=150,verbose_name='Nombre')
    rut=models.CharField(max_length=9,unique=True, verbose_name='RUT')
    fecha_registro=models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion=models.DateTimeField(auto_now=True)
    fecha_actualización=models.DateTimeField(auto_now_add=True)
    edad=models.PositiveIntegerField(default=0)
    comunidad=models.ForeignKey(comunidad, on_delete=models.SET_NULL, null=True)    
    correo=models.CharField(max_length=150,verbose_name='Correo')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='habitante'
        verbose_name_plural='habitantes'
        db_table='habitante'
        ordering=['id']

