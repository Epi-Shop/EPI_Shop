from django.db import models
from .clientes import Clientes

class Emprestimos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='epi_shops_emprestimos')
    data_emprestimo = models.DateField()
    devolucao_prevista = models.DateField()
    devolucao_efetiva = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"

    def __str__(self):
        return f"Empréstimo para {self.clientes} - {self.data_emprestimo}"