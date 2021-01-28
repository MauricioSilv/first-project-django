from django.shortcuts import render

from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'opiniao': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    products = Produto.objects.get(id=pk)
    context = {
        'produto': products
    }
    return render(request, 'produto.html', context)
