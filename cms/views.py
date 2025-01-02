from django.shortcuts import render
from django.db import connection

# Create your views here.

def dashboard(request):
    try:        
        cursor = connection.cursor()
        cursor.execute("call ListarCursosCMS()")   
        result = cursor.fetchall()        
        i=0
        cursos = [0]*len(result)
        for i in range(0, len(result)):
            cursos[i]=result[i]
            i=i+1
        favicon = request.build_absolute_uri('/img/favicon.png')
        return render(request, 'pages/dashboardcms.html', {'cursos': cursos})
    finally:
            cursor.close()
    


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

