from django.db import models
from .clientes import Clientes
from .epis import Epis
from .pagamentos import Pagamentos

class Historico(models.Model):
    data = models.DateTimeField(auto_now_add=True) # Adicionei um campo data
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='epi_shops_historico_epi')
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='epi_shops_historico_cliente')
    pagamentos = models.ForeignKey(Pagamentos, on_delete=models.CASCADE, related_name='epi_shops_historico_pagamento', null=True, blank=True)
    # outros campos relevantes para o histórico

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"

    def __str__(self):
        return f"Histórico - {self.data}"