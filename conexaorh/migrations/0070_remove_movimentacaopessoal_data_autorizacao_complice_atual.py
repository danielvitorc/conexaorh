# Generated by Django 5.1.7 on 2025-06-23 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conexaorh', '0069_remove_movimentacaopessoal_dias_para_autorizacao_diretor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentacaopessoal',
            name='data_autorizacao_complice_atual',
        ),
    ]
