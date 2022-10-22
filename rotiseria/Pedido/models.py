from django.db import models
from model_utils import Choices


# Create your models here.

class Pedido(models.Model):
    fechaPedido = models.DateField()
    horaEntregaDesde = models.DateTimeField()
    horaEntregaHasta = models.DateTimeField()
    TipoEntrega = models.ForeignKey("TipoEntrega", on_delete=models.CASCADE, null=True)
    Estado = models.ForeignKey("Estado", on_delete=models.CASCADE, null=True)


class Estado(models.Model):
    ESTADO_PEDIDO = Choices("Pendiente", "En preparación", "En camino", "Entregado", "Devuelto", "Cancelado")
    PENDIENTE = "Pendiente"
    estadoPedido = models.CharField(max_length=15, choices=ESTADO_PEDIDO, default=PENDIENTE, unique=True)


class TipoEntrega(models.Model):
    TIPO_ENTREGA = Choices("Delivery", "Retiro")
    tipoEntrega = models.CharField(max_length=8, choices=TIPO_ENTREGA, default="Retiro", unique=True)
