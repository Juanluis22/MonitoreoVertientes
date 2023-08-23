from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.

class Selector(TemplateView):
    
    template_name = 'selector/selector.html'  
    context_object_name = 'listaUser'

