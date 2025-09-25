from django import forms 
from django.core.mail.message import EmailMessage

from .models import *

class NovoContatoForm(forms.ModelForm):
    class Meta:
        model = NaturalPerson
        fields = ['first_name', 'last_name', 'birth_date', 'tax_type', 'tax_id']