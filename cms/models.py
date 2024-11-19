from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

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




class Profesores(models.Model):
    idprofesor = models.AutoField(primary_key=True,null=False)
    rutpasaporte = models.CharField(max_length=50,null=False)    
    nombres = models.CharField(max_length=200,null=True)
    ap_paterno = models.CharField(max_length=200,null=True)
    ap_materno = models.CharField(max_length=200,null=True)
    direccion = models.CharField(max_length=200,null=False)
    comuna = models.CharField(max_length=200,null=False)
    fono= models.CharField(max_length=50,null=False)    
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'profesores'

    def __str__(self):
        return self.nombres + ' ' + self.ap_paterno + ' ' + self.ap_materno


class Cursosabiertos(models.Model):
    idcursoabierto = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fechainicio = models.DateTimeField(null=True)
    fechafin = models.DateTimeField(null=True)
    admisioninicio = models.DateTimeField(null=True)
    admisionfin = models.DateTimeField(null=True)
    imgcurso = models.ImageField(null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'cursosabiertos'
        unique_together = ('idcursoabierto', 'idplan', 'idcurso')

    def __str__(self):
        return Cursos.objects.get(nombre = self.idcurso).nombre + ' ' + str(self.idcursoabierto)



class Tipoasignacionprofesor(models.Model):
    idtipoasignacion = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'tipoasignacion'

    def __str__(self):
        return self.nombre

class AsignacionProfesores(models.Model):
    idasignacion = models.AutoField(primary_key=True,null=False)
    idprofesor = models.ForeignKey(Profesores, on_delete=models.CASCADE,null=True)
    idcursoaberto = models.ForeignKey(Cursosabiertos, on_delete=models.CASCADE,null=True)
    idtipoasignacion = models.ForeignKey(Tipoasignacionprofesor, on_delete=models.CASCADE,null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'asignacionprofesores'
        unique_together = ('idasignacion', 'idprofesor', 'idcursoaberto')

    def __str__(self):
        return self.idprofesor
