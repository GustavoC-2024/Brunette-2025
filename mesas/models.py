from django.db import models

class Mesa(models.Model):  # Nombre en singular
    id = models.AutoField(primary_key=True)  # AutoField para clave primaria autoincremental
    numero = models.IntegerField(unique=True)  # Campo único para el número de mesa
    disponible = models.BooleanField(default=True)  # Simplificación del nombre del campo

    def __str__(self):
        return f"Mesa {self.numero} - {'Disponible' if self.disponible else 'No disponible'}"

    class Meta:
        verbose_name = "Mesa"  # Nombre singular para el admin
        verbose_name_plural = "Mesas"  # Nombre plural para el admin
        ordering = ['numero']  # Ordenar por número de mesa por defecto
