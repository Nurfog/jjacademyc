# Generated by Django 4.2.16 on 2024-11-19 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('diagnostico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancopreguntas',
            name='idcurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.cursos'),
        ),
        migrations.AlterField(
            model_name='bancopreguntas',
            name='idplan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios'),
        ),
    ]
