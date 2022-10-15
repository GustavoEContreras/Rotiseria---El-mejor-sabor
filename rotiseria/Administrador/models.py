from django.db import models


# Create your models here.

class Administrador(models.Model):
    cuil = models.DecimalField(max_digits=8, decimal_places=0, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    MASCULINO = "M"
    FEMENINO = "F"
    SEXO_OPCIONES = (
        (MASCULINO, "M"),
        (FEMENINO, "F"),
    )

    sexo = models.CharField(max_length=1,
                      choices=SEXO_OPCIONES,
                      default=FEMENINO)

