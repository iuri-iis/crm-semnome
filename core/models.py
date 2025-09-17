from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.
class Base(models.Model):
    created_at = models.DateField('Data de Criação', auto_now_add=True)
    modified_at = models.DateField('Data de Modificação', auto_now=True)
    is_active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True