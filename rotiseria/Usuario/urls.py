from django.urls import path
from . import views

app_name = "Usuario"
urlpatterns = [
    path('', views.Usuario, name="Usuario"),
]