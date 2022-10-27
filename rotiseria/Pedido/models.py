from django.db import models
from model_utils import Choices
from Cliente.models import Cliente
from Plato.models import Plato
# Create your models here.

class Pedido(models.Model):
    Persona = models.ForeignKey("Cliente.Cliente",on_delete=models.CASCADE, null=True)
    fechaPedido = models.DateField()
    horaEntregaDesde = models.TimeField()
    horaEntregaHasta = models.TimeField()
    TipoEntrega = models.ForeignKey("TipoEntrega", on_delete=models.CASCADE, null=True)
    Estado = models.ForeignKey("Estado", on_delete=models.CASCADE, null=True)
    platos = models.ManyToManyField(Plato)

    def __str__(self):
        return self.Persona.nombre + ' ' + self.Persona.apellido + '-' + self.Estado.estadoPedido + '-' + self.TipoEntrega.tipoEntrega



class Estado(models.Model):
    ESTADO_PEDIDO = Choices("Pendiente", "En preparación", "En camino", "Entregado", "Devuelto", "Cancelado")
    PENDIENTE = "Pendiente"
    estadoPedido = models.CharField(max_length=15, choices=ESTADO_PEDIDO, default=PENDIENTE, unique=True)

    def __str__(self):
        return self.estadoPedido


class TipoEntrega(models.Model):
    TIPO_ENTREGA = Choices("Delivery", "Retiro")
    tipoEntrega = models.CharField(max_length=8, choices=TIPO_ENTREGA, default="Retiro", unique=True)
    def __str__(self):
        return self.tipoEntrega
