# Generated by Django 5.1.7 on 2025-03-24 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cajas', '0001_initial'),
        ('empleados', '__first__'),
        ('mesas', '0001_initial'),
        ('productos', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('generado_ped', models.BooleanField(default=False)),
                ('fecha_hora_gen_ped', models.DateTimeField(blank=True, null=True)),
                ('proceso_ped', models.BooleanField(default=False)),
                ('fecha_hora_pro_ped', models.DateTimeField(blank=True, null=True)),
                ('listo_ped', models.BooleanField(default=False)),
                ('fecha_hora_lis_ped', models.DateTimeField(blank=True, null=True)),
                ('entregado_ped', models.BooleanField(default=False)),
                ('fecha_hora_ent_ped', models.DateTimeField(blank=True, null=True)),
                ('pagado_ped', models.BooleanField(default=False)),
                ('fecha_hora_pago_ped', models.DateTimeField(blank=True, null=True)),
                ('tipo_pago_ped', models.CharField(blank=True, choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta'), ('Transferencia', 'Transferencia'), ('Otro', 'Otro')], max_length=50, null=True)),
                ('id_caja', models.ForeignKey(db_column='id_caja', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cajas.caja')),
                ('id_empl', models.ForeignKey(db_column='id_empl', null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleados.empleados')),
                ('id_mesa', models.ForeignKey(db_column='id_mesa', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mesas.mesa')),
                ('id_venta', models.ForeignKey(db_column='id_venta', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.ventas')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePed',
            fields=[
                ('id_det_ped', models.AutoField(primary_key=True, serialize=False)),
                ('precio_uni_ped', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_ped', models.PositiveIntegerField()),
                ('sub_total_ped', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_ped', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_prod', models.ForeignKey(db_column='id_prod', on_delete=django.db.models.deletion.CASCADE, to='productos.productos')),
                ('id_pedido', models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedidos')),
            ],
        ),
    ]
