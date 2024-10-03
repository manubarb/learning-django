from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)