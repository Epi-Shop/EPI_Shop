# Importa as bibliotecas necessárias
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate  # Funções de autenticação
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required  # Decorador para exigir login
from django.contrib import messages  # Para exibir mensagens ao usuário

from .forms import CustomUserCreationForm  # Importa o formulário de registro customizado
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# View para registrar um novo usuário
class RegisterView(CreateView):
    form_class = CustomUserCreationForm  # Formulário usado para o registro
    template_name = 'login_app/pages/register.html'  # Template para o formulário de registro
    success_url = reverse_lazy('login')  # URL de redirecionamento após o registro bem-sucedido

    def form_valid(self, form):
        """
        Processa o formulário de registro válido. Exibe uma mensagem de sucesso.
        """
        response = super().form_valid(form)
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return response

# View para fazer login
def login_view(request):
    """
    Processa o login do usuário.
    """
    if request.method == 'POST':  # Verifica se o formulário foi submetido
        username = request.POST.get('username')  # Obtém o nome de usuário do formulário
        senha = request.POST.get('senha')  # Obtém a senha do formulário
        user = authenticate(
            request, username=username, password=senha
        )  # Autentica o usuário usando as credenciais fornecidas

        if user is not None:  # Verifica se a autenticação foi bem-sucedida
            login(request, user)  # Faz o login do usuário
            messages.success(request, 'Login realizado com sucesso!')  # Exibe mensagem de sucesso
            return redirect('index')  # Redireciona para a página 'home' após o login
        else:  # Se a autenticação falhar
            messages.error(request, 'Credenciais inválidas.')  # Exibe mensagem de erro
    return render(request, 'login_app/pages/login.html')  # Renderiza o template de login

# View para fazer logout (requer login)
@login_required  # Garante que apenas usuários logados possam acessar esta view
def logout_view(request):
    """
    Faz o logout do usuário.
    """
    logout(request)  # Faz o logout do usuário
    messages.success(request, 'Logout realizado com sucesso!')  # Exibe mensagem de sucesso
    return redirect('login')  # Redireciona para a página de login após o logout

