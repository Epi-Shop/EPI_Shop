from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(models.Model):
    """
    Modelo de usuário customizado, extendendo o AbstractUser do Django.
    """
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # EmailField valida o formato do email
    
    password = models.CharField(max_length=255, default='futebol123')
    username = models.CharField(max_length=150, unique=True, default='admin')
    
    TIPO_USUARIO_CHOICES = (
        ('Cliente', 'Cliente'),
        ('Funcionario', 'Funcionario'),
        ('Gerente', 'Gerente'),
    )
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES, default='Cliente')
    senha = models.CharField(max_length=255)
    
    def _str_(self):
        return f'{self.usuario}'
    
    class Meta:
        verbose_name_plural = 'Usuarios'


class Cargos(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def _str_(self):
        return f'{self.cargo}'
    
    class Meta:
        verbose_name_plural = 'Cargos'

class Funcionarios(models.Model):
    admissao = models.DateField()
    cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE, related_name='funcionarios_cargos')
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='funcionarios_usuarios')
    
    def _str_(self):
        return f'{self.usuarios} - {self.cargos}'
    
    class Meta:
        verbose_name_plural = 'Funcionários'

class Clientes(models.Model):
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='clientes_usuarios')
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    
    def _str_(self):
        return f'{self.usuarios} - {self.razao_social}'
    
    class Meta:
        verbose_name_plural = 'Clientes'

class Emprestimos(models.Model):
    emprestimo = models.DateField()
    devolucao_prevista = models.DateField()
    devolucao_efetiva = models.DateField()
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='emprestimos_clientes')
    
    def _str_(self):
        return f'Emprestimo de {self.clientes}'
    
    class Meta:
        verbose_name_plural = 'Emprestimos'

class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def _str_(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Categorias'

class Epis(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    fornecedor = models.CharField(max_length=50)
    disponibilidade = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='epis_categorias')
    
    def _str_(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Epis'

class Carrinhos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='carrinhos_clientes')
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='carrinhos_epis')
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def _str_(self):
        return f'{self.clientes} - {self.epis}'
    
    class Meta:
        verbose_name_plural = 'Carrinhos'

class Manutencoes(models.Model):
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='manutencoes_epis')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()
    
    def _str_(self):
        return f'Manutencoes de {self.epis}'
    
    class Meta:
        verbose_name_plural = 'Manutenções'

class Pagamentos(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_compra = models.DateField()
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='pagamentos_clientes')
    
    def _str_(self):
        return f'Pagamento de {self.clientes}'
    
    class Meta:
        verbose_name_plural = 'Pagamentos'

class Historico(models.Model):
    data = models.DateField()
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='historico_epis')
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='historico_clientes')
    pagamentos = models.ForeignKey(Pagamentos, on_delete=models.CASCADE, related_name='historico_pagamentos')
    
    def _str_(self):
        return f'Histórico de {self.clientes}'
    
    class Meta:
        verbose_name_plural = 'Historico'