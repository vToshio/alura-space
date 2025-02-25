from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Não é possível acessar essa página não estando logado.')
        return redirect('login')
    
    dados = Fotografia.objects.filter(publicada=True).order_by('data_fotografia').all()
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request, foto_id: int):
    if not request.user.is_authenticated:
        messages.error(request, 'Não é possível acessar essa página não estando logado.')
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Não é possível acessar essa página não estando logado.')   
        return redirect('login')

    fotografias = []
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            fotografias = Fotografia.objects.filter(nome__icontains=nome).order_by('data_fotografia')

    if 'buscar' in request.GET:
        nome = request.GET['buscar'] 
        
    return render(request, 'galeria/buscar.html', {'cards': fotografias})