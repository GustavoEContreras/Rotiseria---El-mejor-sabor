from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from Pedido.forms import PedidoForm


# Create your views here.

def Pedido(request):
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
