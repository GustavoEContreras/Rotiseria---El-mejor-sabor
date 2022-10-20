from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Administrador(request):
    return render(request,'Administrador/estadoPedidos.html')
