from django.contrib import admin
from Apps.clientes.models import Delivery, Cliente, Tienda, Domicilio
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Delivery)
admin.site.register(Tienda)
admin.site.register(Domicilio)
admin.site.register(Cliente, ClienteAdmin)
