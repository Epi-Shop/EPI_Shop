from django import forms
from django.contrib.auth.forms import UserCreationForm
from epi_shops.models import Usuarios  # Importa de epi_shops

# Define um formulário customizado para criação de usuário
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = Usuarios  # Modelo de usuário associado ao formulário
        fields = ('cpf', 'telefone', 'endereco', 'email', 'tipo_usuario', 'username', 'password1', 'password2')  # Campos a serem exibidos no formulário

    def save(self, commit=True):
        # Salva o usuário sem salvá-lo no banco de dados ainda (commit=False)
        user = super().save(commit=False)

        # Define a senha criptografada usando set_password
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data['email']

        if commit:
            user.save()  # Salva o usuário no banco de dados
        return user
    
class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label="Username", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'})
    )
    password = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
    )
    