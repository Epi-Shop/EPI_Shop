from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm  # Importe o formulário de login também
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criada com sucesso! Seja bem-vindo, {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# View para registro
class RegisterView(CreateView):
    form_class = CustomUserCreationForm  # Formulário customizado
    template_name = 'login_app/pages/register.html'  # Template HTML
    success_url = reverse_lazy('login')  # Redireciona para login

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return response

# View para login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Usando o formulário de login
        if form.is_valid():  # Se o formulário for válido
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Nome correto do campo
            user = authenticate(request, username=username, password=password)  # Autentica o usuário

            if user is not None:  # Se a autenticação for bem-sucedida
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('index')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Credenciais inválidas.')
        else:
            messages.error(request, 'Erro ao processar o formulário.')

    else:
        form = LoginForm()

    return render(request, 'login_app/pages/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

