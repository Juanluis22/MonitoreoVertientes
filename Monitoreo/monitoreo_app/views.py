from pyexpat.errors import messages
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'monitoreo_app/index.html')

def about(request):
    return render(request, 'monitoreo_app/about.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('nombre_de_la_vista_después_del_login')
        else:
            # Usuario no válido, puedes mostrar un mensaje de error
            messages.error(request, 'Correo o contraseña incorrectos, prueba de nuevo.')

    return render(request, 'nombre_de_tu_template_login.html')