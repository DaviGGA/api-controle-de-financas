from rest_framework import serializers
from api.models import Receita, Despesa, Resumo

class ReceitasSerializer(serializers.ModelSerializer):
    '''Serializador da classe Receita'''
    class Meta:
        model = Receita
        fields = '__all__'

class DespesasSerializer(serializers.ModelSerializer):
    '''Serializador da classe Despesa'''
    class Meta:
        model = Despesa
        fields = '__all__'


class ListagemReceitas(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['descricao','valor']

class ListagemDespesas(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['descricao','valor','categoria']

class ResumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resumo
        fields = '__all__'
