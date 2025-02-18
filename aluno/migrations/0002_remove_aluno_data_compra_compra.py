# Generated by Django 5.1.6 on 2025-02-18 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data_compra',
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
    ]
