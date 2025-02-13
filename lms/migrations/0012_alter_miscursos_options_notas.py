# Generated by Django 4.2.16 on 2024-11-19 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0007_delete_notas'),
        ('lms', '0011_alter_cursos_unique_together_remove_cursos_idplan_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscursos',
            options={'verbose_name': 'miscursos'},
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('idnota', models.AutoField(primary_key=True, serialize=False)),
                ('nota', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
                ('idcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.cursos')),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.planestudios')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'notas',
                'unique_together': {('idnota', 'idplan', 'idcurso')},
            },
        ),
    ]
