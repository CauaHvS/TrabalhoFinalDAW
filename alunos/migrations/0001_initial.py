# Generated by Django 3.2.9 on 2021-11-30 03:18

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('ra', models.CharField(max_length=8, verbose_name='Registro Academico')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('imagem', stdimage.models.StdImageField(upload_to='produtos', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, unique=True, verbose_name='Slug')),
                ('nota', models.IntegerField(verbose_name='Nota')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.materia', verbose_name='Materia')),
            ],
            options={
                'verbose_name': 'aluno',
                'verbose_name_plural': 'alunos',
                'ordering': ('nome',),
            },
        ),
    ]