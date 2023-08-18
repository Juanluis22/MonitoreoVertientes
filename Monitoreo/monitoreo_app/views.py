from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'monitoreo_app/index.html')

def about(request):
    return render(request, 'monitoreo_app/about.html')
