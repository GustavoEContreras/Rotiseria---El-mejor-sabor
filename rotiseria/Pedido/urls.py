from django.urls import path
from . import views

app_name = "Pedido"
urlpatterns = [
    path('', views.Pedido, name="Pedido"),
]