from django.db import models

# Create your models here.

class Dados_Imc (models.Model):
    peso = models.SmallIntegerField(blank=True, null=True)
    altura = models.SmallIntegerField(blank=True, null=True)