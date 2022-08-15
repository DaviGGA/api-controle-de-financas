from rest_framework.test import APITestCase
from api.models import Receita, Despesa
from rest_framework import status
from datetime import  datetime


class ResumoTestCase(APITestCase):

    def setUp(self):
        self.receita = Receita.objects.create(
            descricao = 'Salário', valor = 5000, data = datetime.now()
        )
        self.despesa_01 = Despesa.objects.create(
            descricao = 'Supermercado', valor = 500, data = datetime.now(), categoria = 'Alimentação'
        )
        self.despesa_02 = Despesa.objects.create(
            descricao = 'Faculdade', valor = 1500, data = datetime.now(), categoria = 'Educação'
        )
        self.despesa_03 = Despesa.objects.create(
            descricao = 'Curso de Inglês', valor = 1000, data = datetime.now(), categoria = 'Educação'
        )

       
    
    
    def test_calculo_resumo(self):
        '''Teste que testa o cálculo do resumo do mês'''
        response = self.client.get(f'/resumo/{datetime.now().month}/{datetime.now().year}')
        data = response.data
        gasto_por_categoria = str(data['Gasto por categoria'])
        gasto_por_categoria_teste = "<QuerySet [{'categoria': 'Alimentação', 'valor_total': 500.0}, {'categoria': 'Educação', 'valor_total': 2500.0}]>"

        self.assertEqual(data["Receita do Mês"], "R$5000.0")
        self.assertEqual(data["Despesa do Mês"], "R$3000.0")
        self.assertEqual(data["Saldo final do Mês"], "R$2000.0")
        self.assertEqual(gasto_por_categoria,gasto_por_categoria_teste)
        

        

         
    def test_get_em_resumo(self):
        '''Testa a requisição GET do Resumo do mês'''
        response = self.client.get(f'/resumo/{self.receita.data.month}/{self.receita.data.year}')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        
