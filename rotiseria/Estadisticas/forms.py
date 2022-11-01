from django import forms
from django.forms import SelectDateWidget

from Cadete.models import Cadete


class DateInput(forms.DateInput):
    input_type = 'date'


class DateRangeForm(forms.Form):
    Fecha_desde = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Fecha_hasta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(DateRangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['type'] = 'date'


class DateRangeCadeteForm(forms.Form):
    Fecha_desde = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Fecha_hasta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Cadete = forms.ModelChoiceField(queryset=Cadete.objects.all())

    def __init__(self, *args, **kwargs):
        super(DateRangeCadeteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['type'] = 'date'
