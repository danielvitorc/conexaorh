# Generated by Django 5.1.7 on 2025-04-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conexaorh', '0032_alter_requisicaopessoal_n_rp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicaopessoal',
            name='n_rp',
            field=models.CharField(max_length=100),
        ),
    ]
