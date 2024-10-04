from django.db import models
from .epis import Epis

class Manutencoes(models.Model):
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='epi_shops_manutencoes')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"

    def __str__(self):
        return f"Manutenção de {self.epis} - {self.data_inicio}"