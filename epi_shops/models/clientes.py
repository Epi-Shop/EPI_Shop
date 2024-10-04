from django.db import models
from .usuarios import Usuarios

class Clientes(models.Model):
    usuarios = models.OneToOneField(Usuarios, on_delete=models.CASCADE, related_name='epi_shops_cliente')
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.usuarios.first_name} {self.usuarios.last_name} - {self.razao_social}"