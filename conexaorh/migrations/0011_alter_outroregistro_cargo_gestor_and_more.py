# Generated by Django 5.1.7 on 2025-04-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conexaorh', '0010_remove_outroregistro_gestor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outroregistro',
            name='cargo_gestor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='outroregistro',
            name='nome_gestor',
            field=models.CharField(max_length=100),
        ),
    ]
