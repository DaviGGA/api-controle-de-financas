from dataclasses import fields
import email
from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User


class ReceitasSerializer(serializers.ModelSerializer):
    '''Serializador da classe Receita'''
    class Meta:
        model = Receita
        fields = ['descricao','valor', 'data']


class DespesasSerializer(serializers.ModelSerializer):
    '''Serializador da classe Despesa'''
    class Meta:
        model = Despesa
        fields = ['descricao','valor', 'data','categoria']


class ListagemReceitas(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['descricao','valor']

class ListagemDespesas(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['descricao','valor','categoria']

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    '''Serializador para Usuário'''
    class Meta:
        model = User
        fields = ['id','email','username','password']
        extra_kwargs ={
            'password' : {'write_only' : True, 'required' : True},
            'email' : {'required' : True},
        }


    def create(self,validated_data):
        '''Cria e retorna um novo usuário'''
        usuario = User.objects.create(  
            email = validated_data['email'],
            username = validated_data['username'],
        )

        usuario.set_password(validated_data['password'])
        usuario.save()

        return usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

