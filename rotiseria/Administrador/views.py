from django.shortcuts import render
from django.http import HttpResponse
from Pedido.models import Pedido

# Create your views here.
"""
def Administrador(request):
    return render(request,'Administrador/estadoPedidos.html')
"""


def pedido_lista(request):
    pedidos = Pedido.objects.all()
    context = {'pedidos': pedidos}
    return render(request, 'Administrador/estadoPedidos.html', context)
