from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Cliente(request):
    return HttpResponse("Hola mundo!")