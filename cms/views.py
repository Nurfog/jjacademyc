from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'pages/dashboard.html')


def cursos(request):
    return render(request, 'pages/cursos.html')


def planestudios(request):
    return render(request, 'pages/planestudios.html')

def cursosabiertos(request):
    return render(request, 'pages/cursosabiertos.html')

def ponderaciones(request):
    return render(request, 'pages/ponderaciones.html')

def profesores(request):
    return render(request, 'pages/profesores.html')

def tipoasignaciones(request):
    return render(request, 'pages/tipoasignaciones.html')

def compras(request):
    return render(request, 'pages/compras.html')

