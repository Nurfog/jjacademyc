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

class ponderaciones(models.Model):
    idponderacion = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    ponderacion = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'ponderaciones'
        unique_together = ('idponderacion', 'idplan', 'idcurso')

    def __str__(self):
        return self.ponderacion

class Notas(models.Model):
    idnota = models.AutoField(primary_key=True,null=False)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    nota = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'notas'
        unique_together = ('idnota', 'idplan', 'idcurso')

    def __str__(self):
        return self.nota


class MisCursos(models.Model):
    idmiscurso = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    
    activo = models.BooleanField(default=True,null=False)


