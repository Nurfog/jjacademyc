# Generated by Django 4.2.16 on 2024-11-19 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='PlanEstudios',
            fields=[
                ('idplan', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'planestudios',
            },
        ),
        migrations.CreateModel(
            name='Tipoasignacionprofesor',
            fields=[
                ('idtipoasignacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'tipoasignacion',
            },
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('idprofesor', models.AutoField(primary_key=True, serialize=False)),
                ('rutpasaporte', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=200)),
                ('fono', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profesores',
            },
        ),
        migrations.CreateModel(
            name='Cursosabiertos',
            fields=[
                ('idcursoaberto', models.AutoField(primary_key=True, serialize=False)),
                ('fechainicio', models.DateTimeField(null=True)),
                ('fechafin', models.DateTimeField(null=True)),
                ('admisioninicio', models.DateTimeField(null=True)),
                ('admisionfin', models.DateTimeField(null=True)),
                ('imgcurso', models.ImageField(null=True, upload_to='')),
                ('activo', models.BooleanField(default=True)),
                ('idasignacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.profesores')),
                ('idcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.cursos')),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios')),
            ],
            options={
                'verbose_name': 'cursosabiertos',
                'unique_together': {('idcursoaberto', 'idplan', 'idcurso')},
            },
        ),
        migrations.AddField(
            model_name='cursos',
            name='idplan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios'),
        ),
        migrations.CreateModel(
            name='ponderaciones',
            fields=[
                ('idponderacion', models.AutoField(primary_key=True, serialize=False)),
                ('ponderacion', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios')),
            ],
            options={
                'verbose_name': 'ponderaciones',
                'unique_together': {('idponderacion', 'idplan')},
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('idnota', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.cursos')),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios')),
            ],
            options={
                'verbose_name': 'notas',
                'unique_together': {('idnota', 'idplan', 'idcurso')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='cursos',
            unique_together={('idcurso', 'idplan')},
        ),
        migrations.CreateModel(
            name='AsignacionProfesores',
            fields=[
                ('idasignacion', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('idcursoaberto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.cursosabiertos')),
                ('idprofesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.profesores')),
                ('idtipoasignacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.tipoasignacionprofesor')),
            ],
            options={
                'verbose_name': 'asignacionprofesores',
                'unique_together': {('idasignacion', 'idprofesor', 'idcursoaberto')},
            },
        ),
    ]
