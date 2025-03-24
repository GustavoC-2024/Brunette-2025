from django.db import models
from django.core.validators import MinLengthValidator

class Cliente(models.Model):  # Nombre en singular
    id = models.AutoField(primary_key=True)  # AutoField para clave primaria autoincremental
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    cuit = models.CharField(max_length=13, unique=True, verbose_name="CUIT", validators=[MinLengthValidator(11)])  # CharField para CUIT
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")  # CharField para teléfono

    def __str__(self):
        return f"{self.nombre} {self.apellido} - CUIT: {self.cuit}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre']  # Ordenar por apellido y nombre
