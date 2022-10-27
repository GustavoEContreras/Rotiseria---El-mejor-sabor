from django.urls import path
from . import views

app_name = "Menu"
urlpatterns = [
    path('Normal', views.MenuNormal, name="menuNormal"),
    path('Vegetariano', views.MenuVegetariano, name="menuVegetariano"),
    path('Diabetico', views.MenuDiabetico, name="menuDiabetico"),
    path('Celiaco', views.MenuCeliaco, name="menuCeliaco"),
    path('Editar',views.EditarMenu, name="editarMenu"),
]