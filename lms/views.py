from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    user = User.objects.get(username=request.user.username, password=request.user.password)
    return render(request, 'pages/dashboard.html')


