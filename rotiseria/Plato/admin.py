from django.contrib import admin
from Plato.models import Plato
from Plato.models import Ingrediente
from Plato.models import TipoPlato
from Plato.models import Precio
# Register your models here.
admin.site.register(Plato)
admin.site.register(Ingrediente)
admin.site.register(TipoPlato)
admin.site.register(Precio)