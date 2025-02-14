from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.middleware.csrf import get_token
import oauth.views 


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def courses(request):
    return render(request, 'pages/courses.html')

def team(request):
    return render(request, 'pages/team.html')

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, 'pages/blog.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def error_404(request):
    return render(request, 'pages/404.html', status=404)

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def login(request):
    return render(request, 'account/login.html')




