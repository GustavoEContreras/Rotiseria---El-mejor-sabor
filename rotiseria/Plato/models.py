from django.db import models
from model_utils import Choices

import Menu.models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcionPlato = models.CharField(max_length=200)
    TipoPlato = models.ForeignKey("Tipoplato", on_delete=models.CASCADE, null=True)
    Precio = models.ForeignKey("Precio", on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField()
    Menu = models.ForeignKey("Menu.Menu", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.nombre + " - " + self.TipoPlato.tipoPlato + " - " + self.Menu.tipo)
class TipoPlato (models.Model):
    TIPO_OPCIONES = Choices('Entrada', 'Plato principal', 'Postre')
    ENTRADA = 'Entrada'
    tipoPlato = models.CharField(max_length=20, choices=TIPO_OPCIONES, default=ENTRADA, unique=True)

    def __str__(self):
        return (self.tipoPlato)
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return (self.nombre)
class Precio(models.Model):
    precio = models.DecimalField(decimal_places=2, max_digits=6)
    Plato = models.ForeignKey("Plato", on_delete=models.CASCADE, null=True)
    fechaActualizacionPrecio = models.DateField()

    def __str__(self):
        return "$" + str(self.precio)