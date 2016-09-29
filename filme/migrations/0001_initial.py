# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-13 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_filme', models.CharField(max_length=200)),
                ('genero_filme', models.CharField(max_length=200)),
                ('sinopse_filme', models.TextField(max_length=200)),
                ('imagem_filme', models.ImageField(upload_to=b'')),
                ('ator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filme.Ator')),
            ],
        ),
    ]
