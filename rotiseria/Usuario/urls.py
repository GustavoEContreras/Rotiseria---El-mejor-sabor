from django.urls import path
from . import views

app_name = "Usuario"
urlpatterns = [
    path('', views.login_index, name="login_index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('createuser', views.create_user, name="create"),
]