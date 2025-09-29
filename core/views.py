from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import *
from contacts import *

from django.apps import apps


__app_config = apps.get_app_config('core')
__app_name = __app_config.name

# Create your views here.
def index(request):
    context = {
        'curso': 'Vários clientes para você',
        'outro': 'Com o nosso app!',
    }
    return render(request, f'{__app_name}/index.html', context)