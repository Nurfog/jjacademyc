import django.contrib.auth.models as auth
from django.contrib.auth.models import User


def get_user(request):
    if request.user.is_authenticated:
        return 1
    else:
        return 0
    
    