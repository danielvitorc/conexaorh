# Generated by Django 5.1.7 on 2025-04-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conexaorh', '0021_rename_data_aprovacao_diretor_movimentacaopessoal_data_autorizacao_diretor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisicaopessoal',
            old_name='observacoes',
            new_name='cursos',
        ),
        migrations.RenameField(
            model_name='requisicaopessoal',
            old_name='nome_colaborador',
            new_name='n_rp',
        ),
        migrations.RemoveField(
            model_name='requisicaopessoal',
            name='gestor',
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='adicionais',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='base',
            field=models.CharField(blank=True, default='N/A', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='beneficios',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='candidato_aprovado',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='centro_custo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='cnh',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='departamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='escolaridade',
            field=models.CharField(blank=True, default='ENSINO MÉDIO COMPLETO', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='exige_viagem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='experiencias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='gestor_imediato',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='habilidades_comportamentais',
            field=models.TextField(default='ADAPTAÇÃO E FLEXIBILIDADE COMUNICAÇÃO ATENÇÃO CONCENTRADA ÉTICA'),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='horario_trabalho_fim',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='horario_trabalho_inicio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='inicio_contrato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='justificativa_outros',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='justificativa_substituicao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='localidade',
            field=models.CharField(blank=True, default='MANAUS', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='matricula',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='motivo_contracao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='outros_cnh',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='principais_atribuicoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='processo_seletivo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='quantidade_vagas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='requisitante',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='salario',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='sexo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='subtituicao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='termino_contrato',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='tipo_cnh',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='tipo_contratacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='requisicaopessoal',
            name='tipo_ponto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
