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
    
    def save(self, *args, **kwargs):        
        super(PlanEstudios, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(PlanEstudios, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(PlanEstudios, self).update(*args, **kwargs)

    def listar(self):
        return PlanEstudios.objects.all()


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
    
    def save(self, *args, **kwargs):        
        super(Cursos, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Cursos, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Cursos, self).update(*args, **kwargs)

    def listar(self):
        return Cursos.objects.all()


class tipoponderacion(models.Model):
    idtipoponderacion = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'tipoponderacion'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):        
        super(tipoponderacion, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(tipoponderacion, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(tipoponderacion, self).update(*args, **kwargs)

    def listar(self):
        return tipoponderacion.objects.all()


class ponderaciones(models.Model):
    idponderacion = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idtipoponderacion = models.ForeignKey(tipoponderacion, on_delete=models.CASCADE,null=True)
    ponderacion = models.IntegerField(null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'ponderaciones'
        unique_together = ('idponderacion', 'idplan')

    def __str__(self):
        return self.ponderacion

    def save(self, *args, **kwargs):        
        super(ponderaciones, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(ponderaciones, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(ponderaciones, self).update(*args, **kwargs)

    def listar(self):
        return ponderaciones.objects.all()


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
        return str(self.nombres + ' ' + self.ap_paterno + ' ' + self.ap_materno)

    def save(self, *args, **kwargs):        
        super(Profesores, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Profesores, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Profesores, self).update(*args, **kwargs)

    def listar(self):
        return Profesores.objects.all()


class Cursosabiertos(models.Model):
    idcursoabierto = models.AutoField(primary_key=True,null=False)
    idplan = models.ForeignKey(PlanEstudios, on_delete=models.CASCADE)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    fechainicio = models.DateTimeField(null=True)
    fechafin = models.DateTimeField(null=True)
    admisioninicio = models.DateTimeField(null=True)
    admisionfin = models.DateTimeField(null=True)
    cupos = models.IntegerField(default=15,null=False)
    horassincronicas = models.IntegerField(default=15, null=False)
    horasasincronicas = models.IntegerField(default=15,null=False)
    imgcurso = models.ImageField(null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'cursosabiertos'
        unique_together = ('idcursoabierto', 'idplan', 'idcurso')

    def __str__(self):
        return Cursos.objects.get(nombre = self.idcurso).nombre + '-' + str(self.idcursoabierto)

    def save(self, *args, **kwargs):        
        super(Cursosabiertos, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Cursosabiertos, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Cursosabiertos, self).update(*args, **kwargs)

    def listar(self):
        return Cursosabiertos.objects.all()


class Tipoasignacionprofesor(models.Model):
    idtipoasignacion = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=200,null=False)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'tipoasignacion'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):        
        super(Tipoasignacionprofesor, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Tipoasignacionprofesor, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(Tipoasignacionprofesor, self).update(*args, **kwargs)

    def listar(self):
        return Tipoasignacionprofesor.objects.all()

class AsignacionProfesores(models.Model):
    idasignacion = models.AutoField(primary_key=True,null=False)
    idprofesor = models.ForeignKey(Profesores, on_delete=models.CASCADE,null=True)
    idcursoabierto = models.ForeignKey(Cursosabiertos, on_delete=models.CASCADE,null=True)
    idtipoasignacion = models.ForeignKey(Tipoasignacionprofesor, on_delete=models.CASCADE,null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'asignacionprofesores'
        unique_together = ('idasignacion', 'idprofesor', 'idcursoabierto')

    def __str__(self):
        return str(self.idprofesor) + '-' + str(self.idcursoabierto) + '-' + str(self.idtipoasignacion)

    def save(self, *args, **kwargs):        
        super(AsignacionProfesores, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(AsignacionProfesores, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(AsignacionProfesores, self).update(*args, **kwargs)

    def listar(self):
        return AsignacionProfesores.objects.all()
    
class CalendarioDetalles(models.Model):
    idcalendariodetalle = models.AutoField(primary_key=True,null=False)
    idcursoabierto = models.ForeignKey(Cursosabiertos, on_delete=models.CASCADE,null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null=True)
    duracion = models.TimeField(null=True)
    activo = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'calendariodetalles'
        unique_together = ('idcalendariodetalle', 'idcursoabierto')

    def __str__(self):
        return str(self.idcursoabierto) + '-' + str(self.idcalendariodetalle)

    def save(self, *args, **kwargs):        
        super(CalendarioDetalles, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):        
        super(CalendarioDetalles, self).delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(CalendarioDetalles, self).update(*args, **kwargs)

    def listar(self):        
        return CalendarioDetalles.objects.all()
    