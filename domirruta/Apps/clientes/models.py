from django.db import models

# Create your models here.


class Cliente(models.Model):
    direccionCliente = models.CharField(max_length=100, help_text="Ingrese la Direccion del Cliente")
