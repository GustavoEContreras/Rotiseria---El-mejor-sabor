"""rotiseria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Cliente.views import index

urlpatterns = [
    path('Administrador/', include('Administrador.urls')),
    path('Cadete/', include('Cadete.urls')),
    path('Cliente/', include('Cliente.urls')),
    path('', index, name="index"),
    path('Estadisticas/', include('Estadisticas.urls')),
    path('Menu/', include('Menu.urls')),
    path('Pedido/', include('Pedido.urls')),
    path('Plato/', include('Plato.urls')),
    path('Usuario/', include('Usuario.urls')),
    path('Vianda/', include('Vianda.urls')),
    path('admin/', admin.site.urls),
]
