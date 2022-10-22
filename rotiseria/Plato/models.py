from django.db import models
from model_utils import Choices
from Menu.models import Menu
from Menu.models import Tipo_Plato

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcionPlato = models.CharField(max_length=200)
    Tipo_Plato = models.ForeignKey("Menu.Tipo_Plato",on_delete=models.CASCADE, null=True)
    Precio = models.ForeignKey("Precio", on_delete=models.CASCADE, null=True)
    activo = models.BooleanField()
    Menu = models.ForeignKey("Menu.Menu",on_delete=models.CASCADE, null=True)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)


class Precio(models.Model):
    precio = models.DecimalField(decimal_places=2,max_digits=6)
    codigoPlato = models.ForeignKey("Plato", on_delete=models.CASCADE, null=True)
    fechaActualizacionPrecio = models.DateField()


