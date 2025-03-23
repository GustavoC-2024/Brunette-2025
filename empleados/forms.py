from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empleados

class EmpleadoForm(UserCreationForm):
    dni_empl = forms.IntegerField(
        label="DNI",
        help_text="Ingrese el número de DNI del empleado (7-8 dígitos).",
    )
    nombre_empl = forms.CharField(label="Nombre", max_length=50)
    apellido_empl = forms.CharField(label="Apellido", max_length=50)
    domicilio_empl = forms.CharField(label="Domicilio", max_length=50)
    telefono_empl = forms.IntegerField(
        label="Teléfono",
        help_text="Ingrese el número de teléfono del empleado (9-12 dígitos).",
        required=False,
    )
    correo_empl = forms.EmailField(label="Correo Electrónico", max_length=100, required=False)
    rango_emp = forms.ChoiceField(label="Rango", choices=Empleados.RANGOS)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'dni_empl', 'nombre_empl', 'apellido_empl', 'domicilio_empl', 'telefono_empl', 'correo_empl', 'rango_emp']