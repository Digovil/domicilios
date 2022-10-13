from django.urls import path
from Apps.personas.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
