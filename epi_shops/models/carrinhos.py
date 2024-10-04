from django.db import models
from .clientes import Clientes
from .epis import Epis

class Carrinhos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='epi_shops_carrinhos')
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='epi_shops_carrinhos')
    quantidade = models.IntegerField(default=0)
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def __str__(self):
        return f"Carrinho de {self.clientes} - {self.epis} ({self.quantidade})"