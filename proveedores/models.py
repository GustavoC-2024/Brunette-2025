from django.db import models
from django.core.validators import EmailValidator

class Proveedor(models.Model):  # Nombre en singular
    id = models.AutoField(primary_key=True)  # AutoField para clave primaria autoincremental
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de proveedor")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")  # CharField para teléfono
    correo = models.EmailField(max_length=50, blank=True, null=True, verbose_name="Correo electrónico", validators=[EmailValidator()])  # EmailField para correo
    direccion = models.CharField(max_length=50, verbose_name="Dirección")

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']  # Ordenar por nombre por defecto
