from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def compras(request):
    return render(request, 'pages/compras.html')
