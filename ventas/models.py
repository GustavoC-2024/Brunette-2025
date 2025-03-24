from django.db import models
from cajas.models import Caja
from clientes.models import Cliente
from productos.models import Productos
from django.core.exceptions import ValidationError

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)  # AutoField para clave primaria autoincremental
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli', verbose_name="Cliente")
    id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='id_caja', verbose_name="Caja")
    fecha_venta = models.DateField(auto_now_add=True, verbose_name="Fecha de venta")
    hora_venta = models.TimeField(auto_now_add=True, verbose_name="Hora de venta")
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de venta")  # DecimalField para total
    venta_realizada = models.BooleanField(default=False, verbose_name="Venta realizada")  # BooleanField para estado

    def clean(self):
        if not self.id_caja.abierta_caja:
            raise ValidationError('No se puede registrar la venta porque la caja está cerrada.')

    def __str__(self):
        return f"Venta {self.id_venta} - Cliente: {self.id_cli} - Total: {self.total_venta}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta', '-hora_venta']  # Ordenar por fecha y hora descendente
        
class DetalleVenta(models.Model):
    id_det_venta = models.AutoField(primary_key=True)  # AutoField para clave primaria autoincremental
    id_venta = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='id_venta', verbose_name="Venta")
    id_prod = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_prod', verbose_name="Producto")
    cantidad_prod_venta = models.IntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario")  # DecimalField para precio
    subtotal_det = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")  # DecimalField para subtotal

    def clean(self):
        if self.cantidad_prod_venta <= 0:
            raise ValidationError('La cantidad debe ser mayor que 0.')

    def __str__(self):
        return f"Detalle {self.id_det_venta} - Venta: {self.id_venta} - Producto: {self.id_prod}"

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        ordering = ['id_venta']  # Ordenar por venta