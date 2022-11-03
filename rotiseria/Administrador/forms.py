from django.forms import forms
from django import forms
from django.forms import ModelForm

from Cadete.models import Cadete


class DateInput(forms.DateInput):
    input_type = 'date'


class ActualizarPedidoForm(forms.Form):
    ESTADO_OPCIONES = (
        (1, "Pendiente"), (2, "En preparación"), (3, "En camino"), (4, "Entregado"), (5, "Devuelto"),
        (6, "Cancelado"))

    estadoPedido = forms.ChoiceField(choices=ESTADO_OPCIONES, label=False)
    comentario = forms.CharField(max_length=500, label=False)
