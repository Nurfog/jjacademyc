from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from lms.models import *
from django.db import connection
from django.contrib.auth.models import User
from lms.classes.spMiscursos import *


# Create your views here.

def dashboard(request):
    try:         
        cursor = connection.cursor()
        cursor.execute("call ListarCursos(%s)", [request.user.username])   
        result = cursor.fetchall()
        i=0
        cursos = [0]*len(result)
        for i in range(0, len(result)):
            cursos[i]=result[i]
            i=i+1
        return render(request, 'pages/dashboard.html', {'cursos': cursos})
    finally:
        cursor.close()

    #return render(request, 'pages/dashboard.html')

def compras(request):
    return render(request, 'pages/compras.html')
   

def logout(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')




