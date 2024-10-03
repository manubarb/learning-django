from django.db import models
from django.contrib.auth.models import User

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='pdf/')
    
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)