from django.urls import path, include
from cms import views
from autenticacion.templates import *
from autenticacion.views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('cms/dashboard/', views.dashboard, name='cmsdashboard'),
    path('cms/cursos/', views.compras, name='cmscursos'),
    path('cms/planestudios/', views.planestudios, name='cmsplanestudios'),
    path('cms/cursosabiertos/', views.cursosabiertos, name='cmscursosabiertos'),
    path('cms/ponderaciones/', views.ponderaciones, name='cmsponderaciones'),
    path('cms/profesores/', views.profesores, name='cmsprofesores'),
    path('cms/tipoasignaciones/', views.tipoasignaciones, name='cmsasignaciones'),
    path('cms/compras/', views.compras, name='cmscompras'),
]