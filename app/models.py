from django.db import models
from django.contrib.auth.models import User

# Create your models here.---------------------------------------------------------


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    productos = models.CharField(max_length=100)
    descripcion = models.TextField()
    email = models.CharField(max_length=100)

# class Soporte(models.Model):
#     nombre = models.CharField(max_length=100)
#     area = models.CharField(max_length=100)

class Documentacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    archivo = models.FileField()

class VPN(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    progreso = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    contacto_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class Correo(models.Model):
    remitente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icare_plus = models.BooleanField(default=False)
    ics_lite = models.BooleanField(default=False)
    outlook = models.BooleanField(default=False)
    onebox = models.BooleanField(default=False)
    vpns = models.ManyToManyField(VPN, blank=True)
    tareas = models.ManyToManyField(Tarea, blank=True)
    correos = models.ManyToManyField(Correo, blank=True)
    documentacion = models.ManyToManyField(Documentacion, blank=True)

