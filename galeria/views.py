from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    dados = Fotografia.objects.filter(publicada=True).order_by('data_fotografia').all()
    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request, foto_id: int):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    fotografias = []
    if 'buscar' in request.GET:
        nome = request.GET['buscar']
        if nome:
            fotografias = Fotografia.objects.filter(nome__icontains=nome).order_by('data_fotografia')

    if 'buscar' in request.GET:
        nome = request.GET['buscar'] 
        
    return render(request, 'galeria/buscar.html', {'cards': fotografias})