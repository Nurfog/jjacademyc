# Generated by Django 5.1.2 on 2024-11-09 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('idbanner', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='')),
                ('posicion', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'banner',
            },
        ),
    ]
