from django.urls import path
from . import views

app_name = "Estadisticas"
urlpatterns = [
    path('', views.Estadisticas, name="Estadisticas"),
    path('', views.ListarVentas, name="ListarVentas"),
]