from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Pedido.models import Pedido

# Create your views here.
"""
def Administrador(request):
    return render(request,'Administrador/estadoPedidos.html')
"""


def pedido_lista(request):
    if request.user.is_authenticated and request.user.is_staff:
        pedidos = Pedido.objects.all()
        context = {'pedidos': pedidos}
        return render(request, 'Administrador/estadoPedidos.html', context)
    else:
        return redirect(reverse('Cliente:Index'))
