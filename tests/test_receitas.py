from rest_framework.test import APITestCase
from api.models import Receita
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import  datetime


class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.usuario = User.objects.create(
            email = 'teste@hotmail.com',
            username = 'teste',
            password = '123456',
        )

        
        self.list_url = reverse('Receitas-list')
        self.receita = Receita.objects.create(
            descricao = 'Salário', valor = 100, data = datetime(2000, 1, 1)
        )

   
    def test_get_em_receitas(self):
        '''Testa requisição GET em receitas'''
        response = self.client.get('/receitas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_em_receitas(self):
        '''Testa requisição POST em receitas'''
        data = {
            'descricao' : 'Testing',
            'valor' : 100,
            'data' : '2000-01-01',
            'username' : 'teste'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_receita_por_id(self):
        '''Testa requisição GET especificando id'''
        response = self.client.get(f'/receitas/{self.receita.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_impede_post_mesma_descricao_mes_ano(self):
        '''Teste que impede uma instância de receita com mesma descrição, mes e ano'''
        data = {
            'descricao' : 'Salário',
            'valor' : 100,
            'data' : '2000-01-01',
            'username' : 'Davi'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_permite_post_mesma_descricao_mes_mas_ano_diferente(self):
        '''Teste que verifica se é possível criar uma instância de receita no mesmo mês, mas em ano diferente'''
        data = {
            'descricao' : 'Salário',
            'valor' : 100,
            'data' : '2001-01-01',
            'usuario' : 1
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

