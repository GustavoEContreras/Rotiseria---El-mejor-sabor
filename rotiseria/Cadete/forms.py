from django.forms import forms
from django import forms
from django.forms import ModelForm

from Cadete.models import Cadete


class DateInput(forms.DateInput):
    input_type = 'date'


class CadeteForm(ModelForm):
    class Meta:
        model = Cadete
        fields = ('cuil', 'nombre', 'apellido', 'sexo', 'fechaDeNacimiento', 'Direccion', 'vigenciaCarnet', 'patenteVehiculo', 'zona')

        widgets = {
            'cuil': forms.NumberInput(attrs={'max': "999999999999"}),
            'fechaDeNacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigenciaCarnet': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'patenteVehiculo': forms.TextInput(attrs={'maxlength': 9})
        }

    def __init__(self, *args, **kwargs):
        super(CadeteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
