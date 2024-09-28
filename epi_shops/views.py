from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'epi_shops/global/index.html')  # Renderiza o arquivo HTML('index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!")  # Mensagem de sucesso
            redirect('index.html')
        else:
            messages.error(request, "Usuário ou senha inválidos!")  # Mensagem de erro
            return HttpResponse("<p>Erro ao logar</p>")  # Retornar uma resposta em caso de erro
    
    return render(request, 'epi_shops/global/login.html')


def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        cpf = request.POST['cpf']  # Obter o CPF do formulário 
        telefone = request.POST['telefone']  # Obter o telefone do formulário
        endereco = request.POST['endereco']  # Obter o endereço do formulário

        # Verificar se o CPF já existe
        if Usuarios.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado!")
            return render(request, 'epi_shops/global/mtds_entrada/create_user.html')

        if password == password_confirm:
            user = Usuarios.objects.create_user(username=username, email=email, password=password, cpf=cpf, telefone=telefone, endereco=endereco)  # Adicionar cpf na criação
            user.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('index')  # Redirecionar após a criação
        else:
            messages.error(request, "As senhas não conferem!")
            return HttpResponse("<p>Erro ao criar usuário</p>")
    else:
        return render(request, 'epi_shops/global/mtds_entrada/create_user.html')
def logout_user(request):
    logout(request)
    return redirect('index.html')  # Redireciona para a URL nomeada 'home'

def shop(request):
    return HttpResponse("<p>Shop</p>")

def cargos(request):    
    if request.method == 'POST':
        nome = request.POST['nome']
        
        
        cargo = Cargos.objects.create(cargo=request.POST['cargo'])
        cargo.save()
        return redirect('cargos.html')
    else:
        return render(request, 'epi_shops/global/cargos.html')

