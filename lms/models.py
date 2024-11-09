from django.db import models

class PlanEstudios(models.Model):
    idplan = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'planestudios'
        
    def __str__(self):
        return self.nombre


class Cursos(models.Model):
    idcurso = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200,null=False)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'cursos'
        unique_together = ('idcurso', 'idplan')
    def __str__(self):
        return self.nombre


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

    
    def __str__(self):
        return self.resultado
