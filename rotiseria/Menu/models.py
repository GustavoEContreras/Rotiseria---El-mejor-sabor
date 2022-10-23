from django.db import models
from model_utils import Choices


# Create your models here.

class Menu (models.Model):
    TIPO_MENU = Choices("Normal", "Celíaco", "Vegetariano", "Diabético")
    tipoMenu = models.CharField(max_length=12, choices=TIPO_MENU, default="Normal", unique=True)



"""
class TipoComida(models.Model):
    TIPO = Choices("Entrada", "Plato principal", "Postre")
    opcionPlato = models.CharField(max_length=16, choices=TIPO, default="Entrada", unique=True)
"""