from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.



# Register your models here.

class PlanEstudiosAdmin(admin.ModelAdmin):
    nombre = ('nombre', 'descripcion', 'activo')

admin.site.register(PlanEstudios, PlanEstudiosAdmin)

class CursosAdmin(admin.ModelAdmin):
    nombre = ('idcurso', 'idplan', 'nombre', 'descripcion', 'activo')

admin.site.register(Cursos, CursosAdmin)

