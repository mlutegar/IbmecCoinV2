from django.contrib import admin
from .models import (
    Professor, Turma, Aluno, Grupo, Convite, Item,
    MovimentacaoSaldo, Compra
)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'professor')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email')
    search_fields = ('nome', 'email')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'limite_aluno', 'turma')

@admin.register(Convite)
class ConviteAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'destinatario', 'remetente', 'valido', 'expiracao')
    list_filter = ('valido',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data_criacao', 'turma', 'quantidade_disponivel')
    search_fields = ('nome', 'descricao')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('item', 'aluno', 'data_compra')
    list_filter = ('data_compra',)

@admin.register(MovimentacaoSaldo)
class MovimentacaoSaldoAdmin(admin.ModelAdmin):
    list_display = ('data_movimentacao', 'valor', 'tipo', 'aluno', 'turma')
    list_filter = ('tipo',)
