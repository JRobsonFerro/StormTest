from django.db import models
	
class Ator(models.Model):
	nome = models.CharField(max_length=200)
	pais = models.CharField(max_length=100)
	foto = models.ImageField()
	
class Filme(models.Model):
	nome_filme = models.CharField(max_length=200)
	imagem_filme = models.ImageField()
	genero_filme = models.CharField(max_length=200)
	ator = models.ForeignKey(Ator, on_delete=models.CASCADE)
	sinopse_filme = models.TextField(max_length=200)
	
