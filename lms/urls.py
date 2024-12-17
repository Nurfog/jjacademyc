from django.urls import path, include
from lms import views
from autenticacion.templates import *
from autenticacion.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('lms/dashboard/', views.dashboard, name='dashboard'),
    path('lms/mascursos/', views.compras, name='mascursos'),
    path('lms/logout/', views.logout_page, name='logout'),
    path('lms/profile/', views.profile, name='profile'),     
]