from django import forms
from .models import Empleados

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = [
            'dni_empl', 
            'nombre_empl', 
            'apellido_empl', 
            'domicilio_empl', 
            'telefono_empl', 
            'correo_empl', 
            'rango_emp'
        ]
        labels = {
            'dni_empl': 'DNI',
            'nombre_empl': 'Nombre',
            'apellido_empl': 'Apellido',
            'domicilio_empl': 'Domicilio',
            'telefono_empl': 'Teléfono',
            'correo_empl': 'Correo Electrónico',
            'rango_emp': 'Rango',
        }
        help_texts = {
            'dni_empl': 'Ingrese el número de DNI del empleado (7-8 dígitos).',
            'nombre_empl': 'Ingrese el nombre del empleado.',
            'apellido_empl': 'Ingrese el apellido del empleado.',
            'domicilio_empl': 'Ingrese la dirección del empleado.',
            'telefono_empl': 'Ingrese el número de teléfono del empleado (9-12 dígitos).',
            'correo_empl': 'Ingrese el correo electrónico del empleado.',
            'rango_emp': 'Seleccione el rango del empleado.',
        }
        widgets = {
            'dni_empl': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_empl': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_empl': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio_empl': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_empl': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_empl': forms.EmailInput(attrs={'class': 'form-control'}),
            'rango_emp': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'dni_empl': {
                'required': 'El DNI es obligatorio.',
                'invalid': 'Ingrese un DNI válido (solo números).',
                'unique': 'Este DNI ya está registrado.',
            },
            'nombre_empl': {
                'required': 'El nombre es obligatorio.',
                'max_length': 'El nombre no puede tener más de 50 caracteres.',
            },
            'apellido_empl': {
                'required': 'El apellido es obligatorio.',
                'max_length': 'El apellido no puede tener más de 50 caracteres.',
            },
            'domicilio_empl': {
                'required': 'El domicilio es obligatorio.',
                'max_length': 'El domicilio no puede tener más de 50 caracteres.',
            },
            'telefono_empl': {
                'invalid': 'Ingrese un número de teléfono válido (solo números).',
            },
            'correo_empl': {
                'invalid': 'Ingrese un correo electrónico válido.',
            },
            'rango_emp': {
                'required': 'El rango es obligatorio.',
                'invalid_choice': 'Seleccione un rango válido.',
            },
        }