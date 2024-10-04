<<<<<<< HEAD
# Importa as bibliotecas necessárias
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios  # Importa o modelo de usuário customizado

# Define um formulário customizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
=======
from django import forms
from django.contrib.auth.forms import UserCreationForm
from epi_shops.models import Usuarios # Importa de epi_shops

<<<<<<< Updated upstream
# Define um formulário customizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
>>>>>>> development
    # Classe Meta para configurar o formulário
    class Meta:
        model = Usuarios  # Modelo de usuário associado ao formulário
        fields = (
            'cpf', 'telefone', 'endereco', 'email', 'tipo_usuario', 'username', 'password'
        )  # Campos a serem exibidos no formulário
<<<<<<< HEAD
=======
        help_texts = {
            'username': None,  # Remove o help_text para o campo username
            'password1': None,  # Remove o help_text para o campo password1
            'password2': None,  # Remove o help_text para o campo password2
        }
>>>>>>> development

    # Sobrescreve o método save para criptografar a senha antes de salvar o usuário
    def save(self, commit=True):
        # Chama o método save da classe pai, mas sem salvar no banco de dados ainda (commit=False)
        user = super().save(commit=False)

        # Define a senha criptografada usando set_password (essencial para segurança!)
        user.set_password(self.cleaned_data["password"])
<<<<<<< HEAD

        # Salva o usuário no banco de dados se commit for True (valor padrão)
        if commit:
            user.save()

        # Retorna o objeto user criado
=======
        user.email = self.cleaned_data['email']

        # Salva o usuário no banco de dados se commit for True (valor padrão)
=======

class CustomUserCreationForm(UserCreationForm): # Formulário customizado
    class Meta:
        model = Usuarios
        fields = ('cpf', 'telefone', 'endereco', 'email', 'tipo_usuario', 'username', 'password') # Campos do formulário de registro

    def save(self, commit=True): # Sobrescreve para criptografar a senha
        user = super().save(commit=False) # Salva o usuário
        user.set_password(self.cleaned_data["password"]) # Criptografa a senha
>>>>>>> Stashed changes
        if commit:
            user.save()  # Salva o usuário no banco de dados
>>>>>>> development
        return user