from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Pedido.forms import PedidoForm, PedidoClienteForm


# Create your views here.

def Pedido(request):
    context = {}
    if request.user.is_authenticated and request.user.is_staff:
        nuevo_pedido = None
        if request.method == 'POST':
            pedido_form = PedidoForm(request.POST, request.FILES)
            if pedido_form.is_valid():
                nuevo_pedido = pedido_form.save(commit=True)
                messages.success(request, 'Se ha registrado correctamente el cliente '.format(nuevo_pedido))
                return redirect(reverse('Pedido:registroPedido'))
        else:
            pedido_form = PedidoForm()
        context = {
            'form': pedido_form
        }
        return render(request, 'Pedido/realizarPedido.html', context)
    else:
        return render(request, 'Cliente/index.html', context)


def PedidoCliente(request):
    pedidoCliente_form = PedidoClienteForm()
    context = {
        'form': pedidoCliente_form
    }
    return render(request, 'Pedido/pedidoCliente.html',context)
