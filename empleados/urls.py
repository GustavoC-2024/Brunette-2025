from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_empleado, name='registrar_empleado'),
]