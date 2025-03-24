from django import forms
from .models import Pedidos, DetallePed

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = [
            'id_mesa', 'id_caja', 'id_venta', 'id_empl', 
            'generado_ped', 'proceso_ped', 'listo_ped', 'entregado_ped', 'pagado_ped', 
            'fecha_hora_gen_ped', 'fecha_hora_pro_ped', 'fecha_hora_lis_ped', 'fecha_hora_ent_ped', 'fecha_hora_pago_ped', 
            'tipo_pago_ped'
        ]
        widgets = {
            'fecha_hora_gen_ped': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_pro_ped': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_lis_ped': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_ent_ped': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_hora_pago_ped': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class DetallePedForm(forms.ModelForm):
    class Meta:
        model = DetallePed
        fields = ['id_pedido', 'id_prod', 'precio_uni_ped', 'cantidad_ped', 'sub_total_ped', 'total_ped']
