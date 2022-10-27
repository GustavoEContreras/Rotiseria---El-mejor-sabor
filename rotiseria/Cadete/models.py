from django.db import models

from Persona.models import Persona
from Persona.models import Zona

# Create your models here.

class Cadete(Persona):
    vigenciaCarnet = models.DateField()
    patenteVehiculo = models.CharField(max_length=9)
    zona = models.ForeignKey("Persona.Zona", on_delete=models.CASCADE)
