from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from nucleo.models import *
from django.urls import reverse
from crud.forms import *
# Create your views here.

# Create your views here.



#Vista que muestra el inicio de la pagina antes del Login
class Inicio(TemplateView):
    
    template_name = 'home.html'  
    context_object_name = 'listaUser' 


#Vista para iniciar sesion
class InicioSesion(LoginView):
    template_name = 'login.html'

#Vista para crear un nuevo User
class NuevoUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('nucleo:login') #luego a una pantalla con un mensaje que diga algo como se esta evaluando su cuenta

#Vista basada en funcion que revisa el tipo de usuario que intena logearse
def revision(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('crud:index')  # Redirige al panel de administración
        else:
            return redirect('usuario:selector')  # Redirige al perfil del usuario
    else:
        return redirect('nucleo:login')  # Redirige al formulario de inicio de sesión