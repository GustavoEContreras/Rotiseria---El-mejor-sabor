from django.contrib import admin

# Register your models here.
from Persona.models import Telefono
from Persona.models import Direccion
from Persona.models import Zona
from Persona.models import Persona

admin.site.register(Telefono)
admin.site.register(Direccion)
admin.site.register(Zona)
admin.site.register(Persona)

1234