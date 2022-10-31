from django import forms
from django.forms import ModelForm, TimeField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Usuario.models import UsuarioCliente


class DateInput(forms.DateInput):
    input_type = 'date'


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class UsuarioForm(UserCreationForm):
    class Meta:
        model = UsuarioCliente
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Usuario', 'autocomplete': 'off'}),
            'password1':
                forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'autocomplete': 'off'}),
            'password2':
                forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'autocomplete': 'off'}),
            'email':
                forms.EmailInput(attrs={'placeholder': 'E-mail', 'autocomplete': 'off'})
        }


    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'