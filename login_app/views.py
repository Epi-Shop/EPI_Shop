from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm
from .forms import CustomUserCreationForm  # Importa o formulário customizado

# View para registro
class RegisterView(CreateView):
    """
    View para registrar um novo usuário.
    """
    form_class = CustomUserCreationForm  # Usa o formulário customizado
    template_name = 'login_app/pages/register.html'  # Template HTML para a view
    success_url = reverse_lazy('login')  # Redireciona para login após registrar

    def form_valid(self, form):
        """
        Exibe mensagem de sucesso ao registrar.
        """
        response = super().form_valid(form)  # Salva o usuário
        messages.success(self.request, 'Usuário cadastrado com sucesso!')  # Mensagem
        return response  # Retorna a resposta

# View para login
def login_view(request):
    form = CustomLoginForm()
    if request.method == 'POST':  # Se o método for POST (submit do form)
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Autentica o usuário
            if user is not None:  # Se a autenticação for bem-sucedida
                login(request, user)  # Faz o login do usuário
                messages.success(request, 'Login realizado com sucesso!')  # Exibe mensagem de sucesso
                return redirect('epi_shops/')  # Redireciona para a página 'home' após o login
            else:  # Se a autenticação falhar
                messages.error(request, 'Credenciais inválidas.')  # Exibe mensagem de erro
    return render(request, 'login_app/pages/login.html', {'form': form})  # Renderiza o template de login

@login_required
def logout_view(request):
    """
    Faz o logout do usuário.
    """
    logout(request)  # Faz o logout do usuário
    messages.success(request, 'Logout realizado com sucesso!')  # Exibe mensagem de sucesso
    return redirect('login')  # Redireciona para a página de login após o logout