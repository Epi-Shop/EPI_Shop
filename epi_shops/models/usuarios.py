from django.contrib.auth.models import Permission, AbstractUser, Group
from django.db import models

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
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='epi_shops_usuarios_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='epi_shops_usuarios_user_permissions')

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
        
    def _str_(self):
        return f"{self.first_name} {self.last_name}"
