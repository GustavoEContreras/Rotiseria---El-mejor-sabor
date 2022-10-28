from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Cadete.models import Cadete
from Persona.models import Zona


# Create your views here.

def Estadisticas(request):
    if request.user.is_authenticated and request.user.is_staff:
        cadetes = Cadete.objects.all()
        zonas = Zona.objects.all()
        context = {
            'cadetes': cadetes,
            'zonas': zonas
        }
        return render(request, 'Estadisticas/estadisticas.html', context)
    else:
        return redirect(reverse('Cliente:Index'))
