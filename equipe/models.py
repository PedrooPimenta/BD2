from django.db import models

# Create your models here.
class Equipe(models.Model):
    #nome
    nome = models.CharField(max_length=200)
    #formação academica
    fa =(
        ("G", "Graduação"),
        ("M", "Mestrado"),
        ("D", "Doutorado"),
    )

    formacao_academica = models.CharField(max_length=30, choices=fa, default='G')
    #email
    email = models.EmailField(max_length=100,null=True,blank=True)
    #data e hora de cadastro
    registro_criado = models.DateTimeField(auto_now_add=True)
    #data e hora registro atualizado
    registro_atualizado = models.DateTimeField(auto_now=True)

    #lattes = models.URLField(max_length=200,null=True,blank=True)
    #google_scholar = models.URLField(max_length=200,null=True,blank=True)
    #research_gate = models.URLField(max_length=200,null=True,blank=True)
    #linkedin = models.URLField(max_length=200,null=True,blank=True)
    #orcid = models.URLField(max_length=200,null=True,blank=True)
    #github = models.URLField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.nome