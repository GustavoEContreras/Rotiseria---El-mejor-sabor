from django.db import models
from model_utils import Choices

import Menu.models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcionPlato = models.CharField(max_length=200)
    TipoPlato = models.ForeignKey("Tipoplato", on_delete=models.CASCADE, null=True)
    Precio = models.ForeignKey("Precio", on_delete=models.CASCADE, null=True)
    activo = models.BooleanField()
    Menu = models.ForeignKey("Menu.Menu", on_delete=models.CASCADE, null=True)

class TipoPlato (models.Model):
    TIPO_OPCIONES = Choices('Entrada', 'Plato principal', 'Postre')
    ENTRADA = 'Entrada'
    tipoPlato = models.CharField(max_length=20, choices=TIPO_OPCIONES, default=ENTRADA, unique=True)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)


class Precio(models.Model):
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    codigoPlato = models.ForeignKey("Plato", on_delete=models.CASCADE, null=True)
    fechaActualizacionPrecio = models.DateField()
