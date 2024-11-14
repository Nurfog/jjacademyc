from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from lms import views
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('lms/dashboard/', views.dashboard, name='dashboard'),
    path('lms/mascursos/', views.compras, name='mascursos'),
    path('lms/logout/', views.logout, name='logout'),
    path('lms/profile/', views.profile, name='profile'),
]