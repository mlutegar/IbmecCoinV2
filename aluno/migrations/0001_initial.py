# Generated by Django 5.1.6 on 2025-02-18 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('limite_aluno', models.IntegerField()),
                ('alunos', models.ManyToManyField(to='aluno.aluno')),
                ('lider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupos_liderados', to='aluno.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valido', models.BooleanField()),
                ('expiracao', models.DateField()),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='aluno.aluno')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_enviados', to='aluno.aluno')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
                ('descricao', models.TextField(max_length=200)),
                ('data_criacao', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_compra', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.item')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentacaoSaldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimentacao', models.DateField(auto_now_add=True)),
                ('valor', models.IntegerField()),
                ('tipo', models.CharField(choices=[('C', 'Crédito'), ('D', 'Débito')], max_length=1)),
                ('descricao', models.TextField(max_length=255)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimentacoes', to='aluno.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='AlunoMovimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('movimentacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.movimentacaosaldo')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=50)),
                ('alunos', models.ManyToManyField(to='aluno.aluno')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.professor')),
            ],
        ),
        migrations.AddField(
            model_name='movimentacaosaldo',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.turma'),
        ),
        migrations.AddField(
            model_name='item',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.turma'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.turma'),
        ),
    ]
