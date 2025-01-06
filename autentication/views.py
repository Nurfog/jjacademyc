from django.shortcuts import render, redirect
from django.contrib.auth import login
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.provider import GoogleProvider

def google_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirigir a la página de inicio si ya está autenticado
    return render(request, 'account/google_login.html')

def signup(request):
    if request.method == 'POST':
        # Lógica para manejar el registro de usuario
        pass
    return render(request, 'account/signup.html')

def login_view(request):
    if request.method == 'POST':
        # Lógica para manejar el inicio de sesión
        pass
    return render(request, 'account/login.html')

def logout_view(request):
    # Lógica para manejar el cierre de sesión
    return redirect('home')  # Redirigir a la página de inicio después de cerrar sesión