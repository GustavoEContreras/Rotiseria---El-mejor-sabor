from django import forms
from django.forms import ModelForm, TimeField

from Pedido.models import Pedido


class DateInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ('Persona', 'fechaPedido', 'horaEntregaDesde', 'horaEntregaHasta', 'TipoEntrega', 'Estado', 'platos',
                  'Cadete')
        widgets = {
            'fechaPedido': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'horaEntregaDesde': TimePickerInput(),
            'horaEntregaHasta': TimePickerInput
        }

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PedidoClienteForm(ModelForm):
    class Meta:
        model = Pedido
        exclude = ('fechaPedido', 'horaEntregaDesde', 'horaEntregaHasta', 'Estado', 'Cadete', 'Persona', 'platos', 'comentario')

    def __init__(self, *args, **kwargs):
        super(PedidoClienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
