from rest_framework import serializers
from api.models import Receita, Despesa

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


