from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.disciplina


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.AutoField(primary_key=True)
    senha = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    limite_aluno = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, through='AlunoGrupo')

    def __str__(self):
        return self.nome


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
    data_criacao = models.DateField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Compra(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    data_compra = models.DateField()

    def __str__(self):
        return f"{self.aluno.nome} comprou {self.item.nome} em {self.data_compra}"


class MovimentacaoSaldo(models.Model):
    data_movimentacao = models.DateField()
    valor = models.IntegerField()
    tipo = models.CharField(max_length=3)
    aluno_remetente = models.ForeignKey(Aluno, related_name='movimentacoes_enviadas', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f"Movimentação {self.tipo} - {self.valor}"


class AlunoTurma(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)


class AlunoGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)


class AlunoMovimentacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    movimentacao = models.ForeignKey(MovimentacaoSaldo, on_delete=models.CASCADE)
