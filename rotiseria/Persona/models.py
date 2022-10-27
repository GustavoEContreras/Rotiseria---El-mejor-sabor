from django.db import models
from model_utils import Choices

# Create your models here.

class Telefono (models.Model):
    numeroTelefono = models.DecimalField(max_digits=13, decimal_places=0, unique=True, primary_key=True)
    FIJO = "Fijo"
    CELULAR = "Celular"
    TIPO_TELEFONO = Choices("Fijo", "Celular")
    tipoTelefono = models.CharField(max_length=7, choices=TIPO_TELEFONO, default=CELULAR)
    Persona = models.ForeignKey("Persona", on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.numeroTelefono) +' - '+ self.tipoTelefono+' - '+self.Persona.nombre+ " " +self.Persona.apellido)

class Direccion(models.Model):
    barrio = models.CharField(max_length=50)
    calle = models.CharField(max_length=30)
    numero = models.CharField(max_length=5)
    localidad = models.CharField(max_length=60)
    Zona = models.ForeignKey("Zona", on_delete=models.CASCADE)

    def __str__(self):
        return (self.calle +' '+ self.numero+', '+self.localidad)


class Zona(models.Model):
    NORTE = "Norte"
    SUR = "Sur"
    OESTE = "Oeste"
    ESTE = "Este"
    ZONA_OPCIONES = Choices("Norte","Sur","Oeste","Este")
    zona = models.CharField(max_length=5, choices=ZONA_OPCIONES, default=NORTE, unique=True)

    def __str__(self):
        return self.zona


class Persona(models.Model):
    cuil = models.DecimalField(max_digits=11, decimal_places=0, unique=True, primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

    MASCULINO = "M"
    FEMENINO = "F"
    SEXO_OPCIONES = (
        (MASCULINO, "M"),
        (FEMENINO, "F")
    )

    sexo = models.CharField(max_length=1,
                            choices=SEXO_OPCIONES,
                            default=FEMENINO)
    fechaDeNacimiento = models.DateField()

    Direccion = models.ForeignKey("Direccion", on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre + ' ' + self.apellido

