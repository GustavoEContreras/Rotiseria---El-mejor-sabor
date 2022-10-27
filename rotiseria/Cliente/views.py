from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from Cliente.forms import ClienteForm


# Create your views here.

def Index(request):
    return render(request, 'Cliente/index.html')


def SobreNosotros(request):
    return render(request, 'Cliente/nosotros.html')


def RegistroCliente(request):
    nuevo_cliente = None
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILES)
        if cliente_form.is_valid():
            nuevo_cliente = cliente_form.save(commit=True)
            messages.success(request, 'Se ha registrado correctamente el cliente '.format(nuevo_cliente))
            return redirect(reverse('Cliente:registroCliente'))
    else:
        cliente_form = ClienteForm()
    context = {
        'form': cliente_form
    }
    return render(request, 'Cliente/registroCliente.html', context)
