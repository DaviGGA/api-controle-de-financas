from django.contrib import admin
from api.models import Receita, Despesa

class ReceitasAdmin(admin.ModelAdmin):
    '''Configurações do Django Admin da classe Receita'''
    list_display = ('id', 'descricao', 'valor')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10
admin.site.register(Receita,ReceitasAdmin)

class DespesasAdmin(admin.ModelAdmin):
    '''Configurações do Django Admin da classe Despesa'''
    list_display = ('id', 'descricao', 'valor')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao',)
    list_per_page = 10
admin.site.register(Despesa,DespesasAdmin)


