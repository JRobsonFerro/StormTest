from django.contrib import admin
from django import forms

from .models import Filme, Ator

class FilmeAdmin(admin.ModelAdmin):
	list_display=('nome_filme', 'imagem_filme', 'genero_filme', 'ator', 'sinopse_filme')
admin.site.register(Filme, FilmeAdmin)

class AtorAdmin(admin.ModelAdmin):
	list_display=('nome', 'pais', 'foto')
admin.site.register(Ator, AtorAdmin)


	
