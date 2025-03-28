from django.shortcuts import render, redirect
from empleados.forms import EmpleadoForm  # Importa el formulario desde la app empleados
from django.contrib.auth.models import User
from empleados.models import Empleados
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def base(request):
    return render(request, "home/base.html")

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, 'Has cerrado sesión correctamente.')  # Mensaje de confirmación
    return redirect('base')  # Redirige a la página principal

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Cambia 'email' por 'username'
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {username}!')
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





