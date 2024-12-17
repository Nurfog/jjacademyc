from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path ('account/', include('django.contrib.auth.urls')),
    path ('account/logout/', views.logout_page, name='logout'),
]
