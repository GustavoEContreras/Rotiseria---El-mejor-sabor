from django.urls import path
from . import views

app_name = "Administrador"
urlpatterns = [
    path('', views.pedido_lista, name="estadoPedidos"),
]
