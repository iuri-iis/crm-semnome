from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'tax_id', 'tax_type')

@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'first_name', 'tax_id', 'tax_type')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "telephone":
            kwargs["queryset"] = Telephone.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(LegalPerson)
class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'company_name', 'tax_id', 'tax_type')

@admin.register(TaxType)
class TaxTypeAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'id', 'name', 'character_limit')

@admin.register(UseType)
class UseTypeAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'id', 'name')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'modified_at', 'is_active', 'name', 'DDI_Code')