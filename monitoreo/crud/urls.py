from django.urls import path
from crud.views import *

app_name='crud'

urlpatterns = [
    #index
    path("indice/", Indice.as_view(), name='index'),

    #indice general
    path("indiceUser/", IndiceUser.as_view(), name='induser'),
    path("indiceComunidad/", IndiceCom.as_view(), name='indcom'),
    path("indiceHabitante/", IndiceHabit.as_view(), name='indhabit'),
    path("indiceVertiente/", IndiceVert.as_view(), name='indvert'),



    #Listar
    path("lista_comunidad/", ListaComunidad.as_view(), name='listcom'),
    path("lista_user/", ListaUsuarios.as_view(), name='listuser'),
    path("lista_habitante/", ListaHabitante.as_view(), name='listhabit'),
    path("lista_vertiente/", ListaVertiente.as_view(), name='listvert'),
    

    #Creación
    path("nueva_comunidad/", NuevaComunidad.as_view(), name='newcom'),
    path("nuevo_user/", NuevoUser.as_view(), name='newuser'),
    path("nuevo_habitante/", NuevoHabitante.as_view(), name='newhabit'),
    path("nueva_vertiente/", NuevaVertiente.as_view(), name='newvert')
    

]