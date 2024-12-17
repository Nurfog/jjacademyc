from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cms.models import *




class MisCurso(models.Model):
    idmiscurso = models.AutoField(primary_key=True,null=False)
    idcursoabierto = models.ForeignKey(Cursosabierto, on_delete=models.CASCADE, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'miscursos'
    
    def __str__(self):
        return str(self.idmiscurso)

class Nota(models.Model):
    idnota = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'notas'
        unique_together = ('idnota', 'idplan', 'idcurso')

    def __str__(self):
        return self

