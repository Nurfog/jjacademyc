from django.contrib import admin
from .models import *

# Register your models here.


class PlanEstudiosAdmin(admin.ModelAdmin):
    nombre = ('nombre', 'descripcion', 'activo')

admin.site.register(PlanEstudio, PlanEstudiosAdmin)

class CursosAdmin(admin.ModelAdmin):
    nombre = ('idcurso', 'idplan', 'nombre', 'descripcion', 'activo')

admin.site.register(Curso, CursosAdmin)

class ProfesoresAdmin(admin.ModelAdmin):
    nombre = ('idprofesor', 'nombres', 'apellidos', 'email', 'telefono', 'activo')

admin.site.register(Profesore, ProfesoresAdmin)

class AsignacionProfesoresAdmin(admin.ModelAdmin):
    nombre = ('idasignacion', 'idprofesor', 'idcursoaberto', 'idtipoasignacion', 'activo')

admin.site.register(AsignacionProfesore, AsignacionProfesoresAdmin)

class TipoasignacionprofesorAdmin(admin.ModelAdmin):
    nombre = ('idtipoasignacion', 'nombre', 'activo')

admin.site.register(Tipoasignacionprofesor, TipoasignacionprofesorAdmin)

class CursosabiertosAdmin(admin.ModelAdmin):
    nombre = ('idcursoabierto', 'idplan', 'idcurso', 'fechainicio', 'fechafin', 'admisioninicio', 'admisionfin', 'idasignacion', 'imgcurso', 'activo')

admin.site.register(Cursosabierto, CursosabiertosAdmin)

class PonderacionesAdmin(admin.ModelAdmin):
    nombre = ('idponderacion', 'idplan', 'idcurso', 'ponderacion', 'activo')

admin.site.register(ponderacione, PonderacionesAdmin)