from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from Plato.models import Plato, Precio
from Menu.models import Menu

# Create your views here.
"""
def Menu(request):
    return render(request, 'Menu/menu.html')
"""


def MenuNormal(request):
    platos = Plato.objects.filter(Menu__tipo="Normal").filter(activo=True)

    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu normal'
    alerta = ('Para añadir platos a tu carrito, necesitas ingresar a tu cuenta.')
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
        'menu_id': 1,
        'value.plato_id': 0,
        'alerta': alerta
    }

    return render(request, 'Menu/Menu.html', context)


def MenuVegetariano(request):
    platos = Plato.objects.filter(Menu__tipo="Vegetariano").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu vegetariano'
    alerta = ('Para añadir platos a tu carrito, necesitas ingresar a tu cuenta.')
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
        'menu_id': 2,
        'value.plato_id': 0,
        'alerta': alerta
    }
    return render(request, 'Menu/Menu.html', context)


def MenuDiabetico(request):
    platos = Plato.objects.filter(Menu__tipo="Diabetico").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu diabetico'
    alerta = ('Para añadir platos a tu carrito, necesitas ingresar a tu cuenta.')
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
        'menu_id': 3,
        'value.plato_id': 0,
        'alerta': alerta
    }
    return render(request, 'Menu/Menu.html', context)


def MenuCeliaco(request):
    platos = Plato.objects.filter(Menu__tipo="Celiaco").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu Celiaco'
    alerta = ('Para añadir platos a tu carrito, necesitas ingresar a tu cuenta.')
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
        'menu_id': 4,
        'value.plato_id': 0,
        'alerta': alerta
    }
    return render(request, 'Menu/Menu.html', context)


def EditarMenu(request):
    if request.user.is_authenticated and request.user.is_staff:
        platosEnMenu = None
        platosInactivos = None
        MOSTRAR_DETALLE = False
        TIPO_MENU = None
        if request.GET.get("tipoMenu"):
            MOSTRAR_DETALLE = True
            TIPO_MENU = request.GET.get("tipoMenu")
            platos = Plato.objects.filter(Menu__id=TIPO_MENU)
            platosInactivos = platos.filter(activo=False)
            platosEnMenu = platos.filter(activo=True)
        menus = Menu.objects.all()
        context = {
            'menus': menus,
            'platosEnMenu': platosEnMenu,
            'platosInactivos': platosInactivos,
            'MOSTRAR_DETALLE': MOSTRAR_DETALLE,
            'TIPO_MENU': TIPO_MENU
        }
        return render(request, 'Menu/editarMenu.html', context)
    else:
        return redirect(reverse('Cliente:Index'))


def QuitarPlato(request, plato_id, menu_id):
    context = {

    }
    if request.user.is_authenticated and request.user.is_staff:
        plato = Plato.objects.get(pk=plato_id)
        plato.activo = False
        plato.save()

        MOSTRAR_DETALLE = True
        TIPO_MENU = menu_id
        platos = Plato.objects.filter(Menu__id=TIPO_MENU)
        platosInactivos = platos.filter(activo=False)
        platosEnMenu = platos.filter(activo=True)
        menus = Menu.objects.all()
        nombreMenu = Menu.objects.get(pk=TIPO_MENU).tipo
        context = {
            'menus': menus,
            'platosEnMenu': platosEnMenu,
            'platosInactivos': platosInactivos,
            'MOSTRAR_DETALLE': MOSTRAR_DETALLE,
            'TIPO_MENU': TIPO_MENU
        }

        messages.success(request, 'Ha eliminado el plato {} del menu {}.'.format(plato.nombre, nombreMenu))
    return render(request, 'Menu/editarMenu.html', context)


def CambiarPrecioPlato(request, plato_id, menu_id):
    platosInactivos = None
    platosEnMenu = None
    MOSTRAR_DETALLE = False
    TIPO_MENU = menu_id
    if request.user.is_authenticated and request.user.is_staff:
        if request.POST.get("precioPlato"):
            precio_plato = request.POST.get("precioPlato")
            precio_nuevo = Precio()
            precio_nuevo.precio = precio_plato
            precio_nuevo.fechaActualizacionPrecio = date.today()
            plato = Plato.objects.get(pk=plato_id)
            precio_nuevo.Plato = plato
            precio_nuevo.save()

            plato.Precio = precio_nuevo
            plato.save()


            MOSTRAR_DETALLE = True

            platos = Plato.objects.filter(Menu__id=TIPO_MENU)
            platosInactivos = platos.filter(activo=False)
            platosEnMenu = platos.filter(activo=True)
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        'platosEnMenu': platosEnMenu,
        'platosInactivos': platosInactivos,
        'MOSTRAR_DETALLE': MOSTRAR_DETALLE,
        'TIPO_MENU': TIPO_MENU
    }
    return render(request, 'Menu/editarMenu.html', context)

def AgregarPlato(request, menu_id):
    platosEnMenu = None
    platosInactivos = None
    MOSTRAR_DETALLE = False
    TIPO_MENU = menu_id
    if request.user.is_authenticated and request.user.is_staff:
        if request.GET.get("platoMenu"):
            MOSTRAR_DETALLE = True
            plato_id = request.GET.get("platoMenu")
            plato = Plato.objects.get(pk=plato_id)
            plato.activo = True
            plato.save()

            platos = Plato.objects.filter(Menu__id=menu_id)
            platosInactivos = platos.filter(activo=False)
            platosEnMenu = platos.filter(activo=True)

            nombreMenu = Menu.objects.get(pk=TIPO_MENU).tipo
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        'platosEnMenu': platosEnMenu,
        'platosInactivos': platosInactivos,
        'MOSTRAR_DETALLE': MOSTRAR_DETALLE,
        'TIPO_MENU': TIPO_MENU
    }

    messages.success(request, 'Ha agregado el plato {} al menu {}.'.format(plato.nombre, nombreMenu))
    return render(request, 'Menu/editarMenu.html', context)
