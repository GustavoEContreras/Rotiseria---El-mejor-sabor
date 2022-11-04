from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Administrador.forms import ActualizarPedidoForm
from Cadete.models import Cadete
from Pedido.models import Pedido, Estado

# Create your views here.
"""
def Administrador(request):
    return render(request,'Administrador/estadoPedidos.html')
"""


def pedido_lista(request):
    if request.user.is_authenticated and request.user.is_staff:
        pedidos = Pedido.objects.all()
        formEstado = ActualizarPedidoForm()
        context = {
            'pedidos': pedidos,
            'form': formEstado,
        }
        return render(request, 'Administrador/estadoPedidos.html', context)
    else:
        return redirect(reverse('Cliente:Index'))


def pedido_lista_cadete(request):
    if request.user.is_authenticated:
        cadete = Cadete.objects.get(usuario=request.user)

        pedidosCadete = Pedido.objects.filter(Cadete=cadete)
        formEstado = ActualizarPedidoForm()

        context = {
            'pedidos': pedidosCadete,
            'form': formEstado,
        }
        return render(request, 'Administrador/estadoPedidos.html', context)
    else:
        return redirect(reverse('Cliente:Index'))


def pedido_lista_cliente(request):
    if request.user.is_authenticated:
        cliente = request.user.Cliente

        pedidosCliente = Pedido.objects.filter(Persona=cliente)
        formEstado = ActualizarPedidoForm()

        context = {
            'pedidos': pedidosCliente,
            'form': formEstado,
        }
        return render(request, 'Administrador/estadoPedidos.html', context)
    else:
        return redirect(reverse('Cliente:Index'))


def cambiarEstadoPedidoConComentario(request, pedido_id):
    if request.method == 'POST':
        formEstado = ActualizarPedidoForm(request.POST, request.FILES)
        if formEstado.is_valid():
            estado_id = formEstado.cleaned_data['estadoPedido']
            comentario = formEstado.cleaned_data['comentario']

            pedido = Pedido.objects.filter(pk=pedido_id).first()
            estadoPedido = Estado.objects.filter(pk=estado_id).first()
            pedido.Estado = estadoPedido
            pedido.comentario = comentario

            pedido.save()
    if request.user.groups.filter(name='Cadete').exists():
        return redirect(reverse('Administrador:estadoPedidosCadete'))
    else:
        return redirect(reverse('Administrador:estadoPedidos'))
