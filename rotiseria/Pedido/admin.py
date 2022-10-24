from django.contrib import admin

# Register your models here.
from Pedido.models import Pedido
from Pedido.models import Estado
from Pedido.models import TipoEntrega

admin.site.register(Pedido)
admin.site.register(Estado)
admin.site.register(TipoEntrega)