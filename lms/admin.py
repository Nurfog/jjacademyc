from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here.

class PlanEstudiosAdmin(admin.ModelAdmin):
    nombre = ('nombre', 'descripcion', 'activo')

admin.site.register(PlanEstudios, PlanEstudiosAdmin)

class CursosAdmin(admin.ModelAdmin):
    nombre = ('idcurso', 'idplan', 'nombre', 'descripcion', 'activo')

admin.site.register(Cursos, CursosAdmin)

class BancoPreguntasAdmin(admin.ModelAdmin):
    nombre = ('idpregunta', 'idcurso', 'idplan', 'pregunta', 'activo')

admin.site.register(BancoPreguntas, BancoPreguntasAdmin)

class BancoRespuestasAdmin(admin.ModelAdmin):
    nombre = ('idrespuesta', 'idpregunta', 'respuesta', 'activo')

admin.site.register(BancoRespuestas, BancoRespuestasAdmin)

class BancoResultadosAdmin(admin.ModelAdmin):
    nombre = ('idresultado', 'idpregunta', 'idrespuesta', 'resultado', 'activo')

admin.site.register(BancoResultados, BancoResultadosAdmin)
