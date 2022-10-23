from django.db import models



# Create your models here.

class Vianda(models.Model):
    tipoVianda = models.ForeignKey("Menu.Menu", on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaVigencia = models.DateField()
    tipoEntregaVianda = models.ForeignKey("Pedido.TipoEntrega", on_delete=models.CASCADE)

