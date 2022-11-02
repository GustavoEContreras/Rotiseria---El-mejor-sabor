from django.urls import path

from Carrito.views import restar_plato, agregar_plato, limpiar_carrito, eliminar_plato
from . import views

app_name = "Menu"
urlpatterns = [
    path('Normal', views.MenuNormal, name="menuNormal"),
    path('Vegetariano', views.MenuVegetariano, name="menuVegetariano"),
    path('Diabetico', views.MenuDiabetico, name="menuDiabetico"),
    path('Celiaco', views.MenuCeliaco, name="menuCeliaco"),
    path('Editar',views.EditarMenu, name="editarMenu"),
    path('agregar/<int:plato_id>/<int:menu_id>', agregar_plato, name="Add"),
    path('eliminar/<int:plato_id>/<int:menu_id>', eliminar_plato, name="Del"),
    path('restar/<int:plato_id>/<int:menu_id>', restar_plato, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]