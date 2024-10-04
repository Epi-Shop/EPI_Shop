from django.db import models
from .cargos import Cargos
from .usuarios import Usuarios

class Funcionarios(models.Model):
    usuarios = models.OneToOneField(Usuarios, on_delete=models.CASCADE, related_name='epi_shops_funcionario')
    cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE, related_name='epi_shops_funcionarios')
    # Adicione outros campos relevantes para funcionários, se necessário

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def __str__(self):
        return f"{self.usuarios.first_name} {self.usuarios.last_name} - {self.cargos}"