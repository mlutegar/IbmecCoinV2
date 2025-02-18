from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.contenttypes.models import ContentType

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(primary_key=True, unique=True)
    senha = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)  # Relacionamento direto com Aluno

    def __str__(self):
        alunos_nomes = ", ".join(self.alunos.values_list("nome", flat=True))
        return f"{self.disciplina} - Alunos: {alunos_nomes}" if alunos_nomes else self.disciplina


class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    limite_aluno = models.IntegerField()
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE)
    alunos = models.ManyToManyField("Aluno")
    lider = models.ForeignKey("Aluno", on_delete=models.SET_NULL, null=True, blank=True, related_name="grupos_liderados")

    def __str__(self):
        return self.nome

    def validate_aluno_limit(self):
        """Valida se o número de alunos não ultrapassa o limite."""
        if self.alunos.count() > self.limite_aluno:
            raise ValidationError(f"O grupo '{self.nome}' não pode ter mais de {self.limite_aluno} alunos.")


class Convite(models.Model):
    valido = models.BooleanField()
    expiracao = models.DateField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Aluno, related_name='convites_recebidos', on_delete=models.CASCADE)
    remetente = models.ForeignKey(Aluno, related_name='convites_enviados', on_delete=models.CASCADE)

    def __str__(self):
        return f"Convite para {self.destinatario.nome} do grupo {self.grupo.nome}"


class Item(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.FloatField()
    descricao = models.TextField(max_length=200)
    data_criacao = models.DateField(auto_now_add=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    quantidade_disponivel = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nome} (Disponível: {self.quantidade_disponivel})"


class Compra(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    data_compra = models.DateField()

    def __str__(self):
        return f"{self.aluno.nome} comprou {self.item.nome} em {self.data_compra}"




class MovimentacaoSaldo(models.Model):
    TIPOS_MOVIMENTACAO = [
        ("C", "Crédito"),
        ("D", "Débito"),
    ]

    data_movimentacao = models.DateField(auto_now_add=True)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPOS_MOVIMENTACAO)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="movimentacoes")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.valor} ({self.aluno.nome})"
