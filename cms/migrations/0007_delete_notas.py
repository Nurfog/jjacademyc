# Generated by Django 4.2.16 on 2024-11-19 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_remove_profesores_id_profesores_ap_materno_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notas',
        ),
    ]
