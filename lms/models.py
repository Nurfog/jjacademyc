from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
    ponderacion = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'ponderaciones'
        unique_together = ('idponderacion', 'idplan')

    def __str__(self):
        return self.ponderacion

class Notas(models.Model):
    idnota = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nota = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'notas'
        unique_together = ('idnota', 'idplan', 'idcurso')

    def __str__(self):
        return self.nota


class Profesores(models.Model):
    idprofesor = models.AutoField(primary_key=True,null=False)
    rutpasaporte = models.CharField(max_length=50,null=False)    
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=200,null=False)
    comuna = models.CharField(max_length=200,null=False)
    fono= models.CharField(max_length=50,null=False)    
    activo = models.BooleanField(default=True,null=False)



class Cursosabiertos(models.Model):
    idcursoaberto = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fechainicio = models.DateTimeField(null=True)
    fechafin = models.DateTimeField(null=True)
    admisioninicio = models.DateTimeField(null=True)
    admisionfin = models.DateTimeField(null=True)
    idasignacion = models.ForeignKey(Profesores, on_delete=models.CASCADE,null=True)
    imgcurso = models.ImageField(null=True)
    activo = models.BooleanField(default=True,null=False)

class AsignacionProfesores(models.Model):
    idasignacion = models.AutoField(primary_key=True,null=False)
    idprofesor = models.ForeignKey(Profesores, on_delete=models.CASCADE,null=True)
    idcursoaberto = models.ForeignKey(Cursosabiertos, on_delete=models.CASCADE,null=True)
    activo = models.BooleanField(default=True,null=False)


class MisCursos(models.Model):
    idmiscurso = models.AutoField(primary_key=True,null=False)
    idcursoabierto = models.ForeignKey(Cursosabiertos, on_delete=models.CASCADE, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activo = models.BooleanField(default=True,null=False)

