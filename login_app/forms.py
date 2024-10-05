from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from epi_shops.models import Usuarios

# Formulário customizado para registro
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# Formulário de login
class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de Usuário", max_length=150)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    