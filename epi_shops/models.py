from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from .models.cargos import Cargos
from .models.carrinhos import Carrinhos
from .models.categorias import Categorias
from .models.clientes import Clientes
from .models.emprestimos import Emprestimos
from .models.epis import Epis
from .models.funcionarios import Funcionarios
from .models.historico import Historico
from .models.manutencoes import Manutencoes
from .models.pagamentos import Pagamentos
from .models.usuarios import Usuarios
