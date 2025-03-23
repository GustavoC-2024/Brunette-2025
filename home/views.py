from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from empleados.forms import EmpleadoForm  # Importa el formulario desde la app empleados
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from empleados.models import Empleados
from django.contrib.auth import authenticate, login
from django.contrib import messages

def base(request):
    return render(request, "home/base.html")

def login(request):
    return render (request, "home/login.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Cambia 'email' por 'username'
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Redirige a la página principal después del login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'home/login.html')

def registro(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            # Crear el empleado
            empleado = Empleados(
                user=user,
                dni_empl=form.cleaned_data['dni_empl'],
                nombre_empl=form.cleaned_data['nombre_empl'],
                apellido_empl=form.cleaned_data['apellido_empl'],
                domicilio_empl=form.cleaned_data['domicilio_empl'],
                telefono_empl=form.cleaned_data['telefono_empl'],
                correo_empl=form.cleaned_data['correo_empl'],
                rango_emp=form.cleaned_data['rango_emp'],
            )
            empleado.save()
            return redirect('base')  # Redirige a la página principal después del registro
    else:
        form = EmpleadoForm()
    return render(request, 'home/registro.html', {'form': form})




