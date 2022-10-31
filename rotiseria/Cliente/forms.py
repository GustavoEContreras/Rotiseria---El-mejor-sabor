from django.forms import forms
from django import forms
from django.forms import ModelForm

from Cliente.models import Cliente


class DateInput(forms.DateInput):
    input_type = 'date'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('cuil', 'nombre', 'apellido', 'sexo', 'fechaDeNacimiento', 'Direccion')

        widgets = {
            'cuil': forms.NumberInput(attrs={'max': "999999999999"}),
            'fechaDeNacimiento': DateInput(
                attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'data-inputmask': "'alias': 'dd/mm/yyyy'",
                       'data-mask': ''}),
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
