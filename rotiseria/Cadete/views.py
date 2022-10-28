from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from Cadete.forms import CadeteForm


# Create your views here.

def Cadete(request):
    if request.user.is_authenticated and request.user.is_staff:
        nuevo_cadete = None
        if request.method == 'POST':
            cadete_form = CadeteForm(request.POST, request.FILES)
            if cadete_form.is_valid():
                nuevo_cadete = cadete_form.save(commit=True)
                messages.success(request, 'Se ha registrado correctamente el cliente '.format(nuevo_cadete))
                return redirect(reverse('Cadete:registroCadete'))
        else:
            cadete_form = CadeteForm()
        context = {
            'form': cadete_form
        }
        return render(request, 'Cadete/registroCadete.html', context)
    else:
        return redirect(reverse('Cliente:Index'))
