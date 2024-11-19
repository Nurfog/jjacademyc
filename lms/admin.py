from django.contrib import admin
from .models import *
from cms.models import *
# Register your models here.


class MiscursosAdmin(admin.ModelAdmin):
    list_display = ('idmiscurso', 'idcursoabierto', 'username', 'activo')

admin.site.register(MisCursos, MiscursosAdmin)

class NotasAdmin(admin.ModelAdmin):
    list_display = ('idnota', 'idplan', 'idcurso', 'idusuario', 'nota', 'activo')

admin.site.register(Notas, NotasAdmin)