from django.db import models
from model_utils import Choices


# Create your models here.

class Menu(models.Model):
    NORMAL = "Normal"
    CELIACO = "Celiaco"
    VEGETARIANO = "Vegetariano"
    DIABETICO = "Diabetico"
    TIPO_MENU = (
        (NORMAL, "Normal"),
        (CELIACO, "Celiaco"),
        (VEGETARIANO, "Vegetariano"),
        (DIABETICO, "Diabetico")
    )

    tipo = models.CharField(max_length=15, choices=TIPO_MENU, default=NORMAL, unique=True)

