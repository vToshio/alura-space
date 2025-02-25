from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import *
from .models import *

def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password = senha,
            )

            if usuario is not None:
                messages.success(request, f'Usuário {nome} logado com sucesso.')
                auth.login(request,usuario)
                return redirect('index')
            else:
                messages.error(request, f'Erro ao realizar login.')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form' : LoginForm()})


def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha1'].value()
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, f'Usuario {nome} cadastrado com sucesso!')
            return redirect('cadastro')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')