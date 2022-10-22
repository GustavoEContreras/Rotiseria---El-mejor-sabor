from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Pedido(request):
    return render(request, 'Pedido/realizarPedido.html')
