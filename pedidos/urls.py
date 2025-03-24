from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pedidos, name='listar_pedidos'),
    path('<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
