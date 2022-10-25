from django.urls import path
from . import views

app_name = "Plato"
urlpatterns = [
    path('', views.Plato, name="registrar"),
]