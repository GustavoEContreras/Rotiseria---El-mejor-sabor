from django.shortcuts import render
from django.http import HttpResponse
from Plato.models import Plato
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
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
    }
    return render(request, 'Menu/Menu.html', context)


def MenuVegetariano(request):
    platos = Plato.objects.filter(Menu__tipo="Normal").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu vegetariano'
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
    }
    return render(request, 'Menu/Menu.html', context)


def MenuDiabetico(request):
    platos = Plato.objects.filter(Menu__tipo="Normal").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu diabetico'
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
    }
    return render(request, 'Menu/Menu.html', context)


def MenuCeliaco(request):
    platos = Plato.objects.filter(Menu__tipo="Normal").filter(activo=True)
    entradas = platos.filter(TipoPlato__tipoPlato='Entrada')
    platosPrincipales = platos.filter(TipoPlato__tipoPlato='Plato principal')
    postres = platos.filter(TipoPlato__tipoPlato='Postre')
    NOMBRE_MENU = 'Menu Celiaco'
    context = {
        'NOMBRE_MENU': NOMBRE_MENU,
        'entradas': entradas,
        'platosPrincipales': platosPrincipales,
        'postres': postres,
    }
    return render(request, 'Menu/Menu.html', context)


def EditarMenu(request):
    platos = None
    MOSTRAR_DETALLE = False
    TIPO_MENU = None
    if request.GET.get("tipoMenu"):
        MOSTRAR_DETALLE = True
        TIPO_MENU = request.GET.get("tipoMenu")
        platos = Plato.objects.filter(Menu__id=TIPO_MENU).filter(activo=True)
    menus = Menu.objects.all()
    context = {
        'menus': menus,
        'platos': platos,
        'MOSTRAR_DETALLE': MOSTRAR_DETALLE,
        'TIPO_MENU': TIPO_MENU
    }
    return render(request, 'Menu/editarMenu.html', context)

