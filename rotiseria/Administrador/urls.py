from django.urls import path
from . import views

app_name = "Administrador"
urlpatterns = [
    path('', views.pedido_lista, name="estadoPedidos"),
    path('Cadete', views.pedido_lista_cadete, name="estadoPedidosCadete"),
    path('Cliente', views.pedido_lista_cliente, name="estadoPedidoCliente"),
    path('cambiarEstadoPedidoConComentario/<int:pedido_id>', views.cambiarEstadoPedidoConComentario, name="cambiarEstadoPedidoConComentario"),

]
