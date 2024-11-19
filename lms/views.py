from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from lms.models import *


# Create your views here.

def dashboard(request):     
    return render(request, 'pages/dashboard.html')

def compras(request):
    cursos = Cursosabiertos.objects.all()
    return render(request, 'pages/compras.html')

def logout(request):
    return render(request, 'account/logout.html')

def profile(request):
    return render(request, 'pages/profile.html')


