from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'cidade', 'estado', 'ativo', 'criado_em']
    list_filter = ['ativo', 'estado']
    search_fields = ['nome', 'email', 'cpf']
    list_editable = ['ativo']
    ordering = ['nome']
