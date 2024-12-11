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
        cursor.execute("call ListarCursos")   
        cursos = cursor.fetchall()
        i=0
        cursoss = [0]*len(cursos)
        for i in range(0, len(cursos)):
            cursoss[i]=cursos[i]
            i=i+1
        return render(request, 'pages/dashboard.html', {'cursoss': cursoss})
    finally:
        cursor.close()

    #return render(request, 'pages/dashboard.html')

def compras(request):
    
def compras(request):
    return render(request, 'pages/compras.html')
   

def logout(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')


