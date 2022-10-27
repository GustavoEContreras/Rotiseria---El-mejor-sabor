from django import forms
from django.forms import ModelForm

from Plato.models import Plato


class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        exclude = ['activo']


    def __init__(self, *args, **kwargs):
        super(PlatoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
