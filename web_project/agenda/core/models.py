from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    dataEvento = models.DateTimeField(verbose_name='data do evento')
    dataCriacao = models.DateTimeField(auto_now=True, verbose_name='data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
