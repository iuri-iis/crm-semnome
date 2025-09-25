from django.urls import path

from .views import *

app_name='contacts'

urlpatterns = [
    path('', listar_contatos, name='listar_contatos'), 
    path('novo_contato/', novo_contato, name='novo_contato'), 
]