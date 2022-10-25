from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Index(request):
    return render(request, 'Cliente/index.html')


def SobreNosotros(request):
    return render(request, 'Cliente/nosotros.html')


def RegistroCliente(request):
    return render(request, 'Cliente/registroCliente.html')



