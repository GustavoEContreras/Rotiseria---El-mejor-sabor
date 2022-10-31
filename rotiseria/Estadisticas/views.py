from django.shortcuts import render
from django.http import HttpResponse
from Cadete.models import Cadete
from Pedido.models import Pedido
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

def ListarVentas(request):
    fechaDesde = request.GET.get("fechaDesde1")
    fechaHasta = request.GET.get("fechaHasta1")
    pedidos = Pedido.objects.filter(date__range=[fechaDesde, fechaHasta])
    cadetes = Cadete.objects.all()
    zonas = Zona.objects.all()
    context = {
        'pedidos': pedidos,
        'cadetes': cadetes,
        'zonas': zonas
    }
    return render(request, 'Estadisticas/estadisticas.html', context)
