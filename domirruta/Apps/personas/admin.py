from django.contrib import admin
from Apps.personas.models import Persona
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
