from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("Usuario:index"))
    return render(request, 'Usuario/login.html')

def logout_view(request):
    logout(request)
    return render(request, "Usuario/login.html")

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Usuario:login"))
    return render(request, "Cliente/index.html")
