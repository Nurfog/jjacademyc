# Generated by Django 4.2.16 on 2024-11-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_delete_notas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacionprofesores',
            old_name='idcursoaberto',
            new_name='idcursoabierto',
        ),
        migrations.AlterUniqueTogether(
            name='asignacionprofesores',
            unique_together={('idasignacion', 'idprofesor', 'idcursoabierto')},
        ),
    ]
