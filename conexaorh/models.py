from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('gestor', 'Gestor'),
        ('diretor', 'Diretor'),
        ('presidente', 'Presidente'),
        ('rh', 'RH'),
        ('complice','Complice')
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

User = get_user_model()

class RequisicaoPessoal(models.Model):
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    requisitante= models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.FloatField()
    adicionais = models.FloatField(default=0)
    quantidade_vagas = models.IntegerField()
    horario_trabalho_inicio = models.TimeField()
    horario_trabalho_fim = models.TimeField()
    tipo_ponto = models.CharField(max_length=100)
    inicio_contrato = models.DateField()
    termino_contrato = models.DateField()
    tipo_contratacao = models.CharField(max_length=100)
    motivo_contracao = models.CharField(max_length=100)
    beneficios = models.CharField(max_length=100)
    subtituicao = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    justificativa_substituicao = models.CharField(max_length=100)
    justificativa_outros = models.CharField(max_length=100)
    processo_seletivo = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100, default="MANAUS", )
    base = models.CharField(max_length=100 ,default="N/A", )
    sexo = models.CharField(max_length=100)
    exige_viagem = models.CharField(max_length=100)
    cnh = models.CharField(max_length=100)
    tipo_cnh = models.CharField(max_length=100)
    outros_cnh = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=100, default="ENSINO MÉDIO COMPLETO", )
    gestor_imediato = models.CharField(max_length=100)
    centro_custo = models.CharField(max_length=100)
    cursos = models.TextField()
    experiencias = models.TextField()
    habilidades_comportamentais = models.TextField(default="ADAPTAÇÃO E FLEXIBILIDADE COMUNICAÇÃO ATENÇÃO CONCENTRADA ÉTICA")
    principais_atribuicoes = models.TextField()
    candidato_aprovado = models.CharField(max_length=100)
    n_rp = models.CharField(max_length=100)

    # Aprovação do diretor
    status_diretor = models.CharField(
        max_length=20,
        choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")],
        default="pendente"
    )
    data_autorizacao_diretor = models.DateTimeField(null=True, blank=True)

    # Aprovação do presidente
    status_presidente = models.CharField(
        max_length=20,
        choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")],
        default="pendente"
    )
    data_autorizacao_presidente = models.DateTimeField(null=True, blank=True)

    # Aprovação do RH
    status_rh = models.CharField(
        max_length=20,
        choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")],
        default="pendente"
    )
    data_autorizacao_rh = models.DateTimeField(null=True, blank=True)

    dias_para_autorizacao_diretor = models.IntegerField(null=True, blank=True)
    dias_para_autorizacao_presidente = models.IntegerField(null=True, blank=True)
    dias_para_autorizacao_rh = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome_colaborador} - Diretor: {self.get_status_diretor_display()} - Presidente: {self.get_status_presidente_display()} - RH: {self.get_status_rh_display()}"
    
class MovimentacaoPessoal(models.Model):
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    numero = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100, default="MANAUS")
    tipo_movimentacao = models.CharField(max_length=100)
    outro_tipo = models.CharField(max_length=100)
    colaborador_movimentado = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    data_admissao = models.DateField()
    outro_info = models.CharField(max_length=100)
    localidade_atual = models.CharField(max_length=100)
    cargo_atual = models.CharField(max_length=100)
    departamento_atual = models.CharField(max_length=100)
    salario_atual = models.FloatField()
    gestor_atual = models.CharField(max_length=100)
    centro_custo_atual = models.CharField(max_length=100)
    localidade_proposta = models.CharField(max_length=100)
    cargo_proposto = models.CharField(max_length=100)
    departamento_proposto = models.CharField(max_length=100)
    salario_proposto = models.FloatField()
    gestor_proposto = models.CharField(max_length=100)
    centro_custo_proposto = models.CharField(max_length=100)
    data_movimentacao = models.DateField()
    tipo_adicional = models.CharField(max_length=100)
    tipo_ajuda_custo = models.CharField(max_length=100)
    valor_ajuda = models.FloatField()
    periodo =  models.CharField(max_length=100)
    jutificativa_movimentacao = models.CharField(max_length=100)
    outro_justificativa = models.CharField(max_length=100)
    substituicao = models.CharField(max_length=100)
    comentarios = models.TextField()

    status_complice = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_complice = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_complice = models.IntegerField(null=True, blank=True)

    status_gestor_proposto = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_gestor_proposto = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_gestor_proposto = models.IntegerField(null=True, blank=True)

    status_diretor = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_diretor = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_diretor = models.IntegerField(null=True, blank=True)

    status_presidente = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_presidente = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_presidente = models.IntegerField(null=True, blank=True)

    status_rh = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_rh = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_rh = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Registro por {self.nome_gestor} ({self.cargo_gestor}) - {self.data_criacao.strftime('%d/%m/%Y')}"
    
class RequisicaoDesligamento(models.Model):
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    requisitante = models.CharField(max_length=100)
    colaborador_desligado = models.CharField(max_length=100)
    data_desligamento = models.DateField()
    funcao = models.CharField(max_length=100)
    salario = models.FloatField()
    localidade = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    data_admissao = models.DateField()
    centro_custo = models.CharField(max_length=100)
    tipo_desligamento = models.CharField(max_length=100)
    motivo_desligamento = models.CharField(max_length=100)
    outro_motivo = models.CharField(max_length=100)
    justificativa_desligamento = models.TextField()
    tipo_aviso = models.CharField(max_length=100)
    justificativa_aviso = models.TextField()
    substituicao = models.CharField(max_length=100)


    status_diretor = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_diretor = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_diretor = models.IntegerField(null=True, blank=True)

    status_presidente = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_presidente = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_presidente = models.IntegerField(null=True, blank=True)

    status_rh = models.CharField(max_length=20, choices=[("pendente", "Pendente"), ("aprovado", "Aprovado")], default="pendente")
    data_autorizacao_rh = models.DateTimeField(null=True, blank=True)
    dias_para_autorizacao_rh = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Registro por {self.titulo} ({self.cargo}) - {self.data_criacao.strftime('%d/%m/%Y')}"