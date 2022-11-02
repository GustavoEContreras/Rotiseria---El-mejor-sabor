from django.shortcuts import render, redirect
from django.urls import reverse

from Carrito.Carrito import Carrito
from Plato.models import Plato


# Create your views here.

def agregar_plato(request, plato_id, menu_id):
    carrito = Carrito(request)
    print(plato_id)
    plato = Plato.objects.get(id=plato_id)
    carrito.agregar(plato)
    if menu_id == 1:
        return redirect(reverse("Menu:menuNormal"))
    elif menu_id == 2:
        return redirect(reverse("Menu:menuVegetariano"))
    elif menu_id == 3:
        return redirect(reverse("Menu:menuDiabetico"))
    else:
        return redirect(reverse("Menu:menuCeliaco"))



def eliminar_plato(request, plato_id, menu_id):
    carrito = Carrito(request)
    plato = Plato.objects.get(id=plato_id)
    carrito.eliminar(plato)
    if menu_id == 1:
        return redirect(reverse("Menu:menuNormal"))
    elif menu_id == 2:
        return redirect(reverse("Menu:menuVegetariano"))
    elif menu_id == 3:
        return redirect(reverse("Menu:menuDiabetico"))
    else:
        return redirect(reverse("Menu:menuCeliaco"))


def restar_plato(request, plato_id, menu_id):
    carrito = Carrito(request)
    plato = Plato.objects.get(id=plato_id)
    carrito.restar(plato)
    if menu_id == 1:
        return redirect(reverse("Menu:menuNormal"))
    elif menu_id == 2:
        return redirect(reverse("Menu:menuVegetariano"))
    elif menu_id == 3:
        return redirect(reverse("Menu:menuDiabetico"))
    else:
        return redirect(reverse("Menu:menuCeliaco"))


def limpiar_carrito(request, menu_id):
    carrito = Carrito(request)
    carrito.limpiar()
    if menu_id == 1:
        return redirect(reverse("Menu:menuNormal"))
    elif menu_id == 2:
        return redirect(reverse("Menu:menuVegetariano"))
    elif menu_id == 3:
        return redirect(reverse("Menu:menuDiabetico"))
    else:
        return redirect(reverse("Menu:menuCeliaco"))
