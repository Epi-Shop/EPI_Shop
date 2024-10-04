from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

<<<<<<< Updated upstream
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
=======
from .forms import CustomUserCreationForm
>>>>>>> Stashed changes

class RegisterView(CreateView): # View para registro
    """
    View para registrar um novo usuário.
    """
    form_class = CustomUserCreationForm # Usa o formulário customizado
    template_name = 'login_app/pages/register.html' # Template HTML para a view
    success_url = reverse_lazy('login') # Redireciona para login após registrar

    def form_valid(self, form):
        """
        Exibe mensagem de sucesso ao registrar.
        """
        response = super().form_valid(form) # Salva o usuário
        messages.success(self.request, 'Usuário cadastrado com sucesso!') # Mensagem
        return response # Retorna a resposta


def login_view(request): # View para login
    """
    Processa o login do usuário.
    """
    if request.method == 'POST': # Se o método for POST (submit do form)
        username = request.POST.get('username') # Pega o nome de usuário do formulário
        senha = request.POST.get('senha') # Pega a senha do formulário
        user = authenticate(request, username=username, password=senha) # Autentica o usuário

        if user is not None: # Se a autenticação for bem-sucedida
            login(request, user)  # Faz o login do usuário
<<<<<<< Updated upstream
            messages.success(request, 'Login realizado com sucesso!')  # Exibe mensagem de sucesso
            return redirect('index')  # Redireciona para a página 'home' após o login
        else:  # Se a autenticação falhar
            messages.error(request, 'Credenciais inválidas.')  # Exibe mensagem de erro
    return render(request, 'login_app/pages/login.html')  # Renderiza o template de login
=======
            messages.success(request, 'Login realizado com sucesso!')  # Mensagem
            return redirect('epi_list') # Redireciona para a página principal 'epi_list'
        else: # Se a autenticação falhar
            messages.error(request, 'Credenciais inválidas.')  # Mensagem
    return render(request, 'login_app/pages/login.html') # Renderiza o template para GET
>>>>>>> Stashed changes


@login_required # Decorador: requer login para acessar essa view
def logout_view(request):
    """
    Faz o logout do usuário.
    """
<<<<<<< Updated upstream
    logout(request)  # Faz o logout do usuário
    messages.success(request, 'Logout realizado com sucesso!')  # Exibe mensagem de sucesso
    return redirect('login')  # Redireciona para a página de login após o logout

=======
    logout(request) # Faz o logout
    messages.success(request, 'Logout realizado com sucesso!') # Mensagem
    return redirect('login') # Redireciona para o login
>>>>>>> Stashed changes
