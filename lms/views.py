from django.shortcuts import render
from lms.models import *
from django.db import connection
from lms.classes.spMiscursos import *
from lms.classes.classes import *
from autenticacion.urls import *
from django.shortcuts import redirect

# Create your views here.

def dashboard(request):
    if get_user(request)==1:
        try:        
            cursor = connection.cursor()
            cursor.execute("call ListarMisCursos(%s)", [request.user.username])   
            result = cursor.fetchall()        
            i=0
            cursos = [0]*len(result)
            for i in range(0, len(result)):
                cursos[i]=result[i]
                i=i+1
            return render(request, 'pages/dashboard.html', {'cursos': cursos})
        finally:
            cursor.close()
    else:
        return redirect("/account/")

    #return render(request, 'pages/dashboard.html')

def compras(request):
    try:         
        cursor = connection.cursor()
        cursor.execute("call VentaCursos")   
        result = cursor.fetchall()
        i=0
        cursos = [0]*len(result)
        for i in range(0, len(result)):
            cursos[i]=result[i]
            i=i+1
        return render(request, 'pages/compras.html', {'cursos': cursos})
    finally:
        cursor.close()
    
   

def logout_page(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')




