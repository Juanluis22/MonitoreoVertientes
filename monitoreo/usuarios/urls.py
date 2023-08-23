from django.urls import path
from usuarios.views import *

app_name='usuario'

urlpatterns = [

    #Selector de vertientes
    path("selector/", Selector.as_view(), name='selector'),

]