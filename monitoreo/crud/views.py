from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from nucleo.models import *
from django.urls import reverse
from crud.forms import *
# Create your views here.


#Indice principal
class Indice(TemplateView):
    
    template_name = 'index/index.html'  
    context_object_name = 'listaUser'





#USER

#Indice para User
class IndiceUser(TemplateView):
    
    template_name = 'usuario/index/index.html'  
    context_object_name = 'listaUser'


#Vista para crear un nuevo User
class NuevoUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'usuario/new/newUsuario.html'

    def get_success_url(self):
        return reverse('crud:listuser')


#Vista para poder ver una lista de los User
class ListaUsuarios(ListView):
    model = User  # Especifica el modelo que deseas mostrar en la lista
    template_name = 'usuario/list/listUsuario.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'listaUser' 






#COMUNIDAD

#Indice para Comunidad
class IndiceCom(TemplateView):
    
    template_name = 'comunidad/index/index.html'  
    context_object_name = 'listaUser'




#Vista para crear una nueva Comunidad
class NuevaComunidad(CreateView):
    model = comunidad
    form_class = ComunidadForm
    template_name = 'comunidad/new/newComunidad.html'

    def get_success_url(self):
        return reverse('crud:listcom')

#Vista para poder ver una lista de las comunidades
class ListaComunidad(ListView):
    model = comunidad  # Especifica el modelo que deseas mostrar en la lista
    template_name = 'comunidad/list/listComunidad.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'listaComunidad' 
    





#VERTIENTE


#Indice para Vertiente
class IndiceVert(TemplateView):
    
    template_name = 'vertiente/index/index.html'  
    context_object_name = 'listaUser'


#Vista para crear una nueva Vertiente
class NuevaVertiente(CreateView):
    model = vertiente
    form_class = VertienteForm
    template_name = 'vertiente/new/newVertiente.html'

    def get_success_url(self):
        return reverse('crud:listvert') 

#Vista para poder ver una lista de las vertientes
class ListaVertiente(ListView):
    model = vertiente  # Especifica el modelo que deseas mostrar en la lista
    template_name = 'vertiente/list/listVertiente.html' # Nombre de la plantilla a utilizar
    context_object_name = 'listaVertiente' 






#HABITANTE

#Indice para Habitante
class IndiceHabit(TemplateView):
    
    template_name = 'habitante/index/index.html'  
    context_object_name = 'listaUser'


#Vista para crear un nuevo Habitante
class NuevoHabitante(CreateView):
    model = habitantes
    form_class = HabitanteForm
    template_name = 'habitante/new/newHabitante.html'

    def get_success_url(self):
        return reverse('crud:listhabit')


#Vista para poder ver una lista de los habitantes
class ListaHabitante(ListView):
    model = habitantes  # Especifica el modelo que deseas mostrar en la lista
    template_name = 'habitante/list/listHabitante.html'  # Nombre de la plantilla a utilizar
    context_object_name = 'listaHabitantes' 

