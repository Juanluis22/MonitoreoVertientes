from django.urls import path
from nucleo.views import *

app_name='nucleo'

urlpatterns = [

    path("revision/", revision, name='revision'),

    path("login/", InicioSesion.as_view(), name='login'),

]
