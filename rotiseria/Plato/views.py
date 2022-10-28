from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Cadete.forms import CadeteForm
from Plato.forms import PlatoForm


# Create your views here.

def Plato(request):
    if request.user.is_authenticated and request.user.is_staff:
        nuevo_plato = None
        if request.method == 'POST':
            plato_form = PlatoForm(request.POST, request.FILES)
            plato_form.instance.activo = True
            if plato_form.is_valid():
                nuevo_plato = plato_form.save(commit=True)
                messages.success(request, 'Se ha registrado correctamente el cliente '.format(nuevo_plato))
                return redirect(reverse('Plato:registrar'))
        else:
            plato_form = PlatoForm()
        context = {
            'form': plato_form
        }
        return render(request, 'Plato/registroPlato.html', context)
    else:
        return redirect(reverse('Cliente:Index'))
