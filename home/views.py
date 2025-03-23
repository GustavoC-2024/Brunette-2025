from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from empleados.forms import EmpleadoForm  # Importa el formulario desde la app empleados

def base(request):
    return render(request, "home/base.html")

def login(request):
    return render (request, "home/login.html")



def registro(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)  # Crea el formulario con los datos enviados
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda el empleado en la base de datos
            return redirect('base')  # Redirige a la vista 'base' después de guardar
    else:
        form = EmpleadoForm()  # Crea un formulario vacío para GET

    # Pasa el formulario a la plantilla
    return render(request, 'home/registro.html', {'form': form})




