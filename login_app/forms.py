from django import forms
from django.contrib.auth.forms import UserCreationForm
from epi_shops.models import Usuarios # Importa de epi_shops


class CustomUserCreationForm(UserCreationForm): # Formulário customizado
    class Meta:
        model = Usuarios
        fields = ('cpf', 'telefone', 'endereco', 'email', 'tipo_usuario', 'username', 'password') # Campos do formulário de registro

    def save(self, commit=True): # Sobrescreve para criptografar a senha
        user = super().save(commit=False) # Salva o usuário
        user.set_password(self.cleaned_data["password"]) # Criptografa a senha
        if commit:
            user.save()  # Salva o usuário no banco de dados
        return user