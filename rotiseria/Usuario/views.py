from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from Cliente.forms import ClienteForm
from Usuario.forms import UsuarioForm


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


def create_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Usuario:index"))
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, request.FILES)
        cliente_form = ClienteForm(request.POST, request.FILES)

        if usuario_form.is_valid() and cliente_form.is_valid():
            nuevo_cliente = cliente_form.save(commit=True)
            usuario_form.instance.Cliente = nuevo_cliente
            nuevo_usuario = usuario_form.save(commit=True)
            messages.success(request, 'Se ha registrado correctamente el usuario'.format(nuevo_usuario))
            return redirect(reverse('Usuario:login'))
    else:
        usuario_form = UsuarioForm()
        cliente_form = ClienteForm()
    context = {
        'form': usuario_form,
        'formC': cliente_form
    }
    return render(request, "Usuario/crearUsuario.html",context)
