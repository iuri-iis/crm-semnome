from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.http import HttpResponse
from django.template import loader

from .models import *
from .forms import *

# Create your views here.

def listar_contatos(request):
    context = {
        'curso': 'Django Framework',
        'outro': 'Django é massa!',
    }
    return render(request, 'listar_contatos.html', context)

def novo_contato(request):
    if str(request.user) == 'POST':
        return redirect('listar_contatos')
    
    if str(request.method) == 'POST':
        form = NovoContatoForm(request.POST, request.FILES)

        if form.is_valid():
            contato = form.save(commit=True)
            print(f'Nome: {contato.first_name}')
            print(f'Sobrenome: {contato.last_name}')
            print(f'Data de Nascimento: {contato.birth_date}')
            print(f'Documento Fiscal: {contato.tax_type}')
            print(f'ID Fiscal: {contato.tax_id}')
                
            messages.success(request, 'Cliente salvo com sucesso')
            form = NovoContatoForm()
        else:
            messages.error(request, 'Erro ao salvar cliente')

    else:
        form = NovoContatoForm()
        
    context = {
        'form': form
    }

    return render(request, 'novo_contato.html', context)