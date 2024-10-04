from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Modelo de Usuário customizado
class Usuarios(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, default='futebol123')
    username = models.CharField(max_length=150, unique=True, default='admin')
    TIPO_USUARIO_CHOICES = (
        ('Cliente', 'Cliente'),
        ('Funcionario', 'Funcionario'),
        ('Gerente', 'Gerente'),
    )
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES, default='Cliente')
    senha = models.CharField(max_length=255)
    
    # Define related_name para evitar conflitos
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='epi_usuarios_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='epi_usuarios_user_permissions')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.groups.exists():
            if self.tipo_usuario == 'Cliente':
                grupo, _ = Group.objects.get_or_create(name='Cliente')
            elif self.tipo_usuario == 'Funcionario':
                grupo, _ = Group.objects.get_or_create(name='Funcionario')
            elif self.tipo_usuario == 'Gerente':
                grupo, _ = Group.objects.get_or_create(name='Gerente')
            self.groups.add(grupo)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Demais Modelos
class Cargos(models.Model):
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def _str_(self):
        return f"{self.cargo} - {self.descricao}"

class Funcionarios(models.Model):
    admissao = models.DateField()
    cargos = models.ForeignKey(Cargos, on_delete=models.CASCADE, related_name='funcionarios_cargos')
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='funcionarios_usuarios')

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"

    def _str_(self):
        return f"{self.usuarios.first_name} {self.usuarios.last_name} - {self.cargos.cargo}"

class Clientes(models.Model):
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='clientes_usuarios')
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def _str_(self):
        return f"{self.usuarios.first_name} {self.usuarios.last_name} - {self.razao_social}"

class Emprestimos(models.Model):
    emprestimo = models.DateField()
    devolucao_prevista = models.DateField()
    devolucao_efetiva = models.DateField()
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='emprestimos_clientes')

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"

    def _str_(self):
        return f"Empréstimo para {self.clientes} - {self.emprestimo}"


class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def _str_(self):
        return f"{self.nome} - {self.descricao}"

class Epis(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    fornecedor = models.CharField(max_length=50)
    disponibilidade = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='epis_categorias')

    class Meta:
        verbose_name = "Epis"
        verbose_name_plural = "Epis"

    def _str_(self):
        return f"{self.nome} - {self.cliente}"


class Carrinhos(models.Model):
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='carrinhos_clientes')
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='carrinhos_epis')
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"

    def _str_(self):
        return f"Carrinho de {self.clientes} - {self.epis} - {self.quantidade}"

class Manutencoes(models.Model):
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='manutencoes_epis')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()

    class Meta:
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"

    def _str_(self):
        return f"Manutenção de {self.epis} - {self.data_inicio}"

class Pagamentos(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_compra = models.DateField()
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='pagamentos_clientes')

    class Meta:
        verbose_name = "Pagaamento"
        verbose_name_plural = "Pagamentos"

    def _str_(self):
        return f"Pagamento de {self.clientes} - {self.valor}"

class Historico(models.Model):
    data = models.DateField()
    epis = models.ForeignKey(Epis, on_delete=models.CASCADE, related_name='historico_epis')
    clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='historico_clientes')
    pagamentos = models.ForeignKey(Pagamentos, on_delete=models.CASCADE, related_name='historico_pagamentos')

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"

    def _str_(self):
        return f"Histórico - {self.data}"