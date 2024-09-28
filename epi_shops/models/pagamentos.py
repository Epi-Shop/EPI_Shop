from django.db import models
from .clientes import Clientes

class Pagamentos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='epi_shops_pagamentos')
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_compra = models.DateField()

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return f"Pagamento de {self.clientes} - {self.valor}"