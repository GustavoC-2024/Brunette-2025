from django.db import models
from mesas.models import Mesa
from cajas.models import Caja
from ventas.models import Ventas
from empleados.models import Empleados
from productos.models import Productos

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, db_column='id_mesa')
    id_caja = models.ForeignKey(Caja, on_delete=models.SET_NULL, null=True, db_column='id_caja')
    id_venta = models.ForeignKey(Ventas, on_delete=models.SET_NULL, null=True, db_column='id_venta')
    id_empl = models.ForeignKey(Empleados, on_delete=models.SET_NULL, null=True, db_column='id_empl')

    generado_ped = models.BooleanField(default=False)
    fecha_hora_gen_ped = models.DateTimeField(null=True, blank=True)

    proceso_ped = models.BooleanField(default=False)
    fecha_hora_pro_ped = models.DateTimeField(null=True, blank=True)

    listo_ped = models.BooleanField(default=False)
    fecha_hora_lis_ped = models.DateTimeField(null=True, blank=True)

    entregado_ped = models.BooleanField(default=False)
    fecha_hora_ent_ped = models.DateTimeField(null=True, blank=True)

    pagado_ped = models.BooleanField(default=False)
    fecha_hora_pago_ped = models.DateTimeField(null=True, blank=True)

    TIPO_PAGO_CHOICES = [
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Otro', 'Otro'),
    ]
    tipo_pago_ped = models.CharField(max_length=50, choices=TIPO_PAGO_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'Pedido {self.id_pedido} - Mesa {self.id_mesa}'

class DetallePed(models.Model):
    id_det_ped = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, db_column='id_pedido')
    id_prod = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column='id_prod')
    precio_uni_ped = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_ped = models.PositiveIntegerField()
    sub_total_ped = models.DecimalField(max_digits=10, decimal_places=2)
    total_ped = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle {self.id_det_ped} - Pedido {self.id_pedido}'

