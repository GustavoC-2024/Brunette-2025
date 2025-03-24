from django.contrib import admin
from .models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'disponible')  # Campos a mostrar en la lista
    list_filter = ('disponible',)  # Filtros laterales
    search_fields = ('numero',)  # Búsqueda por número de mesa
