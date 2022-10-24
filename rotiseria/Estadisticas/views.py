from django.shortcuts import render
from django.http import HttpResponse
from Cadete.models import Cadete
from Persona.models import Zona


# Create your views here.

def Estadisticas(request):
    cadetes = Cadete.objects.all()
    zonas = Zona.objects.all()
    context = {
        'cadetes': cadetes,
        'zonas': zonas
    }
    return render(request, 'Estadisticas/estadisticas.html', context)
