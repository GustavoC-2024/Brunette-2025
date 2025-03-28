# Generated by Django 5.1.7 on 2025-03-24 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cajas', '0001_initial'),
        ('clientes', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField(auto_now_add=True, verbose_name='Fecha de venta')),
                ('hora_venta', models.TimeField(auto_now_add=True, verbose_name='Hora de venta')),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total de venta')),
                ('venta_realizada', models.BooleanField(default=False, verbose_name='Venta realizada')),
                ('id_caja', models.ForeignKey(db_column='id_caja', on_delete=django.db.models.deletion.DO_NOTHING, to='cajas.caja', verbose_name='Caja')),
                ('id_cli', models.ForeignKey(db_column='id_cli', on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['-fecha_venta', '-hora_venta'],
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_det_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_prod_venta', models.IntegerField(verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio unitario')),
                ('subtotal_det', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('id_prod', models.ForeignKey(db_column='id_prod', on_delete=django.db.models.deletion.DO_NOTHING, to='productos.productos', verbose_name='Producto')),
                ('id_venta', models.ForeignKey(db_column='id_venta', on_delete=django.db.models.deletion.DO_NOTHING, to='ventas.ventas', verbose_name='Venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalles de Venta',
                'ordering': ['id_venta'],
            },
        ),
    ]
