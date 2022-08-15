from rest_framework.test import APITestCase
from api.models import Despesa
from rest_framework import status
from django.urls import reverse
from datetime import  datetime


class DespesasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.despesa = Despesa.objects.create(
            descricao = 'Supermercado', valor = 100, data = datetime(2000, 1, 1), categoria = 'Alimentação'
        )

   
    def test_get_em_despesas(self):
        '''Testa a requisição GET em despesas'''
        response = self.client.get('/despesas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_em_despesas(self):
        '''Testa a requisição POST em despesas'''
        data = {
            'descricao' : 'Testing',
            'valor' : 100,
            'data' : '2000-01-01',
            'categoria' : 'Moradia'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_despesa_por_id(self):
        '''Testa requisição GET em despesas especificando id'''
        response = self.client.get(f'/despesas/{self.despesa.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_impede_post_mesma_descricao_mes_ano(self):
        '''Teste que verifica o impedimento uma instância com mesma descrição, mes e ano'''
        data = {
            'descricao' : 'Supermercado',
            'valor' : 100,
            'data' : '2000-01-01',
            'categoria' : 'Alimentação'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_permite_post_mesma_descricao_mes_mas_ano_diferente(self):
        '''Teste que verifica se é possível criar uma instância de despesa com mesma descrição,mesmo mês, porém anos diferentes'''
        data = {
            'descricao' : 'Supermercado',
            'valor' : 100,
            'data' : '2001-01-01',
            'categoria' : 'Alimentação'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

