from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def dados(request):
    return render(request, 'dados.html')

def cursos(request):
    return render(request, 'cursos.html')

def hobbies(request):
    return render(request, 'hobbies.html')