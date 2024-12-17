from django.db import models
from lms.models import *
from cms.models import *

# Create your models here.

class BancoPregunta(models.Model):
    idpregunta = models.AutoField(primary_key=True,null=False)
    idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    idplan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancopreguntas'
    def __str__(self):
        return self.pregunta

class BancoRespuesta(models.Model):
    idrespuesta = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(BancoPregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancorespuestas'
    def __str__(self):
        return self.respuesta

    
class BancoResultado(models.Model):
    idresultado = models.AutoField(primary_key=True,null=False)
    idpregunta = models.ForeignKey(BancoPregunta, on_delete=models.CASCADE)
    idrespuesta = models.ForeignKey(BancoRespuesta, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'bancoresultados'
        unique_together = ('idresultado', 'idpregunta', 'idrespuesta')

    
    def __str__(self):
        return self.resultado