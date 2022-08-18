from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import FormRegistro, FormInicioSesion 



#Vistas para el sitio

#Vista para el registro de usuarios
def RegistroView(request):
    form = FormRegistro()
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada correctamente por ' + user)
            return redirect('login')
        
        messages.error(request, 'Error al crear la cuenta. Intente nuevamente.')
    context = {'form': form}
    return render(request, 'cuenta/register.html', context)

#Vista para el login de usuarios
def LoginView(request):
    if request.method == "POST":
        form = FormInicioSesion(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, 'Bienvenido ' + username)
                return HttpResponseRedirect("/")
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Error al iniciar sesión. Intente nuevamente.')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'registro/login.html', context)

#Vistas para el logout de usuarios
def LogoutView(request):
    context = {}
    return render(request, 'registro/logout.html', context)

def HomeView(request):
    context = {}
    return render(request, 'home.html', context)

#Vista con lo que se muestra en el mail de restauracion de contraseña
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registro/reset_password/password_reset.html'
    email_template_name = 'registro/reset_password/password_reset_email.html'
    subject_template_name = 'registro/reset_password/password_reset_subject.txt'