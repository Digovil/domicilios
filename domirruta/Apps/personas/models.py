from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el Nombre del cliente")
    telefono = models.CharField(max_length=100, help_text="Ingrese el numero de telefono")
    identificacion = models.CharField(max_length=100, help_text="Ingrese identificacion")
    def __str__(self):
        return self.nombre