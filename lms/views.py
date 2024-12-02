from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from lms.models import *
from django.db import connection
from lms.classes import spMiscursos


# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username is not None:
            results = spMiscursos.ListarMiscursos(request, username)
            return render(request, 'pages/dashboard.html', {'results': results})
    return render(request, 'pages/dashboard.html')

def compras(request):  
    return render(request, 'pages/compras.html')

def logout(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')


