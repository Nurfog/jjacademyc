# Generated by Django 4.2.16 on 2024-12-16 20:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_rename_asignacionprofesores_asignacionprofesore_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0012_alter_miscursos_options_notas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MisCursos',
            new_name='MisCurso',
        ),
        migrations.RenameModel(
            old_name='Notas',
            new_name='Nota',
        ),
    ]