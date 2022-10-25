from django.urls import path
from . import views

app_name = "Cadete"
urlpatterns = [
    path('', views.Cadete, name="registroCadete"),
]