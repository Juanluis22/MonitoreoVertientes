from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# Create your views here.



#Vista que muestra el inicio de la pagina antes del Login
class Inicio(TemplateView):
    
    template_name = 'home.html'  
    context_object_name = 'listaUser' 


#Vista para iniciar sesion
class InicioSesion(LoginView):
    template_name = 'login.html'


#Vista basada en funcion que revisa el tipo de usuario que intena logearse
def revision(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('crud:index')  # Redirige al panel de administración
        else:
            return redirect('usuario:selector')  # Redirige al perfil del usuario
    else:
        return redirect('nucleo:login')  # Redirige al formulario de inicio de sesión