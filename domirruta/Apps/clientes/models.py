from tabnanny import verbose
from django.db import models
from Apps.personas.models import Persona
# Create your models here.

class Delivery(models.Model):
    placa = models.CharField(max_length=100, verbose_name="Placa")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name="Persona")
    def __str__(self):
        return self.placa
class Cliente(models.Model):
    direccionCliente = models.CharField(max_length=100, help_text="Direccion del Cliente")
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, verbose_name="Persona")
    def __str__(self):
        return self.direccionCliente
class Tienda(models.Model):
    direccionTienda = models.CharField(max_length=100, help_text="Direccion de la Tienda")
    producto = models.CharField(max_length=100, help_text="producto")
    def __str__(self):
        return self.direccionTienda

class Domicilio(models.Model):
    direccionDomicilio = models.CharField(max_length=100, help_text="Direccion del Domicilio")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    Tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, verbose_name="Tienda")
    Delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, verbose_name="Delivery")
    def __str__(self):
        return self.direccionDomicilio