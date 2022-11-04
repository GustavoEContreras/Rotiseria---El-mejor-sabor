import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Cadete.models import Cadete
from Carrito.Carrito import Carrito
from Pedido.forms import PedidoForm, PedidoClienteForm
from Pedido.models import Estado
from Plato.models import Plato
from Usuario.models import UsuarioCliente


# Create your views here.

def Pedido(request):
    context = {}
    if request.user.is_authenticated and request.user.is_staff:
        nuevo_pedido = None
        if request.method == 'POST':
            pedido_form = PedidoForm(request.POST, request.FILES)
            if pedido_form.is_valid():
                nuevo_pedido = pedido_form.save(commit=True)
                messages.success(request, 'Se ha registrado correctamente el pedido')
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
    """
        Datos de la persona:
            Nombre + Apellido
            Dirección (barrio calle número)
        """
    personaCliente = request.user.Cliente
    """
    Obtener cadete segun la zona
    """
    zonaCliente = personaCliente.Direccion.Zona
    cadete = Cadete.objects.filter(zona=zonaCliente).first()
    """
    Obtener listado de platos del carrito
        Nombre
        Precio
    """
    carrito = Carrito(request)

    """
    Detalles de entrega
        Fecha
        Hora de entrega
    """
    fechaActual = datetime.date.today()
    horaActual = datetime.datetime.now()
    horaEntregaDesde = horaActual + datetime.timedelta(minutes=30)
    horaEntregaHasta = horaActual + datetime.timedelta(minutes=60)
    nuevo_pedido = None
    if request.method == 'POST':
        pedidoCliente_form = PedidoClienteForm(request.POST, request.FILES)
        nuevo_pedido = pedidoCliente_form.save(commit=False)
        nuevo_pedido.fechaPedido = fechaActual
        nuevo_pedido.horaEntregaDesde = horaEntregaDesde
        nuevo_pedido.horaEntregaHasta = horaEntregaHasta

        nuevo_pedido.Persona = personaCliente
        estadoPendiente = Estado.objects.get(pk=1)
        nuevo_pedido.Estado = estadoPendiente
        #Asignar o no cadete
        print(carrito.carrito)
        nuevo_pedido.save()
        for key in carrito.carrito:
            platoRegistrado = Plato.objects.get(pk=key)
            print(platoRegistrado)
            nuevo_pedido.platos.add(platoRegistrado)

        if pedidoCliente_form.is_valid():
            messages.success(request, 'Pedido generado con éxito! Gracias por elegirnos. --EL MEJOR SABOR--'.format(nuevo_pedido))
            return redirect(reverse('index'))
    else:
        pedidoCliente_form = PedidoClienteForm()


    context = {
        'form': pedidoCliente_form,
        'cliente': personaCliente,
        'cadete': cadete,
        'horaEntregaDesde': horaEntregaDesde,
        'horaEntregaHasta': horaEntregaHasta,
        'fechaActual': fechaActual,
    }
    return render(request, 'Pedido/pedidoCliente.html', context)



