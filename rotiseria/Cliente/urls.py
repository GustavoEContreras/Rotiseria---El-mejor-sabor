from django.urls import path
from . import views

app_name = "Cliente"
urlpatterns = [
    path('', views.Index, name="Index"),
    path('sobreNosotros/', views.SobreNosotros, name="SobreNosotros"),
    path('registroCliente/', views.RegistroCliente, name="RegistroCliente"),
]