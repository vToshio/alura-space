from django.shortcuts import render
from .forms import *

def login(request):
    return render(request, 'usuarios/login.html', {'form' : LoginForm()})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html', {'form': CadastroForm()})