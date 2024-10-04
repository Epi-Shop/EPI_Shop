from django.db import models

class Cargos(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo