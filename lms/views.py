from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from lms.models import *
from django.db import connection
from django.contrib.auth.models import User


# Create your views here.

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def compras(request):
    
    return render(request, 'pages/compras.html',)

def logout(request):
    return render(request, 'pages/login.html')

def profile(request):
    return render(request, 'pages/profile.html')


