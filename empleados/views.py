from django.shortcuts import render, redirect
from .forms import EmpleadoForm

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_la_vista')  # Redirige a otra vista después de guardar
    else:
        form = EmpleadoForm()
    return render(request, 'home/registro.html', {'form': form})
