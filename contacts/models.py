from django.db import models
from core.models import Base

from django.db.models import signals
#from django.template.defaultfilters import slugify

# Create your models here.


#Definição de informações geográficas

class Country(Base):
    name = models.CharField('País', max_length=100)
    DDI_Code = models.CharField('DDI', max_length=5)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

class State(Base):
    name = models.CharField('Estado', max_length=100)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class City(Base):
    name = models.CharField('Cidade', max_length=255)
    id_state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class PostalCode(Base):
    postal_code = models.CharField('Código postal', max_length=30)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'CEP'
        verbose_name_plural = 'CEPs'

#Definição de tipos de pessoa física e jurídica (CPF e CNPJ ou outros documentos, se considerar outros países)
class TaxType(Base):
    name = models.CharField('Documento Fiscal', max_length=40)
    character_limit = models.IntegerField('Limite de caracteres', default=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Documento Fiscal'
        verbose_name_plural = 'Documentos Fiscais'

#Definição básica de pessoa
class Person(Base):
    tax_id = models.CharField('ID Fiscal', max_length=20)    
    tax_type = models.ForeignKey(TaxType, on_delete=models.PROTECT)

    def __str__(self):
        return self.tax_id
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

class NaturalPerson(Person): #Pessoa física
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=255)
    birth_date = models.DateField('Data de Nascimento')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Pessoa física'
        verbose_name_plural = 'Pessoas físicas'
                                  
class LegalPerson(Person): #Pessoa jurídica
    company_name = models.CharField('Nome da empresa', max_length=255)
    company_creation_date = models.DateField('Data de Criação da Companhia')
    #industry

    class Meta:
        verbose_name = 'Pessoa jurídica'
        verbose_name_plural = 'Pessoas jurídicas'


class UseType(Base):
    name = models.CharField('Tipo de uso', max_length=30)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


#Definição de e-mail
class Email(Base):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=128)
    use_type = models.ForeignKey(UseType, on_delete=models.PROTECT)
    is_main_email = models.BooleanField('Email principal?', default=False)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

#Definição de telefone
class Telephone(Base):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField('Número de telefone', max_length=50)
    id_DDI = models.ForeignKey(Country, on_delete=models.PROTECT)
    use_type = models.ForeignKey(UseType, on_delete=models.PROTECT)
    is_main_phone = models.BooleanField('Telefone principal?', default=False)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

class Address(Base):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street_name = models.CharField('Rua', max_length=120)
    number = models.CharField('Número', max_length=5)
    addon_address = models.CharField('Complemento', max_length=200)
    id_cep = models.ForeignKey(PostalCode, on_delete=models.PROTECT)
    use_type = models.ForeignKey(UseType, on_delete=models.PROTECT)
    is_main_address = models.BooleanField('Endereço principal?', default=False)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
