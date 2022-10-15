from django.urls import path
from . import views

app_name = "Vianda"
urlpatterns = [
    path('', views.Vianda, name="Vianda"),
]