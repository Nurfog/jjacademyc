from django.db import models
from lms.models import *
from cms.models import *

# Create your models here.

class BancoPreguntas(models.Model):
    idpregunta = models.AutoField(primary_key=True,null=False)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancopreguntas'
    def __str__(self):
        return self.pregunta

class BancoRespuestas(models.Model):
    idrespuesta = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(BancoPreguntas, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancorespuestas'
    def __str__(self):
        return self.respuesta

    
class BancoResultados(models.Model):
    idresultado = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(BancoPreguntas, on_delete=models.CASCADE)
    idrespuesta = models.ForeignKey(BancoRespuestas, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancoresultados'
        unique_together = ('idresultado', 'idpregunta', 'idrespuesta')

    
    def __str__(self):
        return self.resultado