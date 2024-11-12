# Generated by Django 4.2.16 on 2024-11-11 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('idnota', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.cursos')),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.planestudios')),
            ],
            options={
                'verbose_name': 'notas',
                'unique_together': {('idnota', 'idplan', 'idcurso')},
            },
        ),
        migrations.CreateModel(
            name='ponderaciones',
            fields=[
                ('idponderacion', models.AutoField(primary_key=True, serialize=False)),
                ('ponderacion', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.cursos')),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.planestudios')),
            ],
            options={
                'verbose_name': 'ponderaciones',
                'unique_together': {('idponderacion', 'idplan', 'idcurso')},
            },
        ),
        migrations.RemoveField(
            model_name='bancorespuestas',
            name='idpregunta',
        ),
        migrations.RemoveField(
            model_name='bancoresultados',
            name='idpregunta',
        ),
        migrations.RemoveField(
            model_name='bancoresultados',
            name='idrespuesta',
        ),
        migrations.DeleteModel(
            name='BancoPreguntas',
        ),
        migrations.DeleteModel(
            name='BancoRespuestas',
        ),
        migrations.DeleteModel(
            name='BancoResultados',
        ),
    ]
