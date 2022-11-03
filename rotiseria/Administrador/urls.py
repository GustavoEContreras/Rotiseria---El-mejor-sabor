from django.urls import path
from . import views

app_name = "Administrador"
urlpatterns = [
    path('', views.pedido_lista, name="estadoPedidos"),
    path('cambiarEstadoPedidoConComentario/<int:pedido_id>', views.cambiarEstadoPedidoConComentario, name="cambiarEstadoPedidoConComentario"),

]
