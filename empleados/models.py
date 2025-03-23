from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Empleados(models.Model):
    # Rangos disponibles
    RANGOS = [
        ('COC', 'Cocinero'),
        ('MOZ', 'Mozo'),
        ('CAJ', 'Cajero'),
    ]

    # Relación con el modelo User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos existentes
    dni_empl = models.BigIntegerField(
        unique=True,
        verbose_name="DNI",
        help_text="Ingrese el número de DNI del empleado.",
        validators=[
            MinValueValidator(1000000, message="El DNI debe tener al menos 7 dígitos."),
            MaxValueValidator(99999999, message="El DNI no puede tener más de 8 dígitos.")
        ]
    )
    nombre_empl = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_empl = models.CharField(max_length=50, verbose_name="Apellido")
    domicilio_empl = models.CharField(max_length=50, verbose_name="Domicilio")
    telefono_empl = models.BigIntegerField(
        blank=True,
        null=True,
        verbose_name="Teléfono",
        help_text="Ingrese el número de teléfono del empleado.",
        validators=[
            MinValueValidator(100000000, message="El teléfono debe tener al menos 9 dígitos."),
            MaxValueValidator(999999999999, message="El teléfono no puede tener más de 12 dígitos.")
        ]
    )
    correo_empl = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Correo Electrónico")
    rango_emp = models.CharField(max_length=3, choices=RANGOS, default='MOZ', verbose_name="Rango")

    def __str__(self):
        return f"{self.nombre_empl} {self.apellido_empl}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"