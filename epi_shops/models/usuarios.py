from django.contrib.auth.models import Permission, AbstractUser, Group
from django.db import models

class Usuarios(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    TIPO_USUARIO_CHOICES = (
        ('Cliente', 'Cliente'),
        ('Funcionario', 'Funcionario'),
        ('Gerente', 'Gerente'),
    )
    tipo_usuario = models.CharField(max_length=12, choices=TIPO_USUARIO_CHOICES, default='Cliente')
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='epi_shops_usuarios_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='epi_shops_usuarios_user_permissions')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.groups.exists():  # Só adiciona ao grupo se não estiver em nenhum
            if self.tipo_usuario == 'Cliente':
                grupo, _ = Group.objects.get_or_create(name='Cliente')
            elif self.tipo_usuario == 'Funcionario':
                grupo, _ = Group.objects.get_or_create(name='Funcionario')
            elif self.tipo_usuario == 'Gerente':
                grupo, _ = Group.objects.get_or_create(name='Gerente')
            else:
                grupo, _ = Group.objects.get_or_create(name='Padrão') # Grupo padrão caso tipo_usuario seja inválido
            self.groups.add(grupo)
        

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name}" # Ou self.username se preferir