from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.
def index(request):
    context = {
        'curso': 'Vários clientes para você',
        'outro': 'Com o nosso app!',
    }
    return render(request, 'index.html', context)