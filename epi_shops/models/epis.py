from django.db import models
from .categorias import Categorias

class Epis(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=200)
    quantidade = models.IntegerField(default=0)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    fornecedor = models.CharField(max_length=50)
    disponibilidade = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='epi_shops_epis')


    class Meta:
        verbose_name = "Epi"
        verbose_name_plural = "Epis"

    def __str__(self):
        return f"{self.nome} ({self.quantidade})"