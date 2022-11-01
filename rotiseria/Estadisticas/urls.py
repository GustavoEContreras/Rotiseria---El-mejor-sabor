from django.urls import path
from . import views

app_name = "Estadisticas"
urlpatterns = [
    path('', views.Estadisticas, name="Estadisticas"),
    path('listarVentas', views.ListarVentas, name="ListarVentas"),
    path('listarMenus', views.ListarMenus, name="ListarMenus"),
    path('listarCantidadesEntregadasPorCadete', views.ListarCantidadesEntregadasPorCadete, name="ListarCantidadesEntregadasPorCadete"),
    path('listarPlatosSolicitados', views.ListarPlatosSolicitados, name="ListarPlatosSolicitados"),

]
