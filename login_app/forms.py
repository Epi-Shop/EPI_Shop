# Importa as bibliotecas necessárias
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios  # Importa o modelo de usuário customizado

# Define um formulário customizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    # Classe Meta para configurar o formulário
    class Meta:
        model = Usuarios  # Modelo de usuário associado ao formulário
        fields = (
            'cpf', 'telefone', 'endereco', 'email', 'tipo_usuario', 'username', 'password'
        )  # Campos a serem exibidos no formulário

    # Sobrescreve o método save para criptografar a senha antes de salvar o usuário
    def save(self, commit=True):
        # Chama o método save da classe pai, mas sem salvar no banco de dados ainda (commit=False)
        user = super().save(commit=False)

        # Define a senha criptografada usando set_password (essencial para segurança!)
        user.set_password(self.cleaned_data["password"])

        # Salva o usuário no banco de dados se commit for True (valor padrão)
        if commit:
            user.save()

        # Retorna o objeto user criado
        return user