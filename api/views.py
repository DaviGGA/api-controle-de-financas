from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response

from .models import Receita, Despesa
from .serializer import ReceitasSerializer, DespesasSerializer, ListagemReceitas, ListagemDespesas, ResumoSerializer

class ReceitasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as receitas'''
    queryset = Receita.objects.all()
    serializer_class = ReceitasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']
    

class DespesasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as despesas'''
    queryset = Despesa.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']

class ListaReceitas(generics.ListAPIView):
    def get_queryset(self):
        
        
        queryset = Receita.objects.filter(data__year = self.kwargs['year'] , data__month = self.kwargs['month'])
        return queryset
    
    serializer_class = ListagemReceitas

class ListaDespesas(generics.ListAPIView):
    def get_queryset(self):
        queryset = Despesa.objects.filter(data__month = self.kwargs['month'], data__year = self.kwargs['year'])
        return queryset
    
    serializer_class = ListagemDespesas

class ResumoDoMes(APIView):
    queryset = Receita.objects.none()
    
    def get(self, request, mes, ano):
        receita_do_mes = Receita.objects.filter(data__month = mes, data__year = ano).aggregate(Sum('valor')) ['valor__sum'] or 0
        despesa_do_mes = Despesa.objects.filter(data__month = mes, data__year = ano).aggregate(Sum('valor')) ['valor__sum'] or 0
        saldo = receita_do_mes - despesa_do_mes
        gasto_por_categoria = Despesa.objects.filter(data__month = mes, data__year = ano).values('categoria').annotate(valor_total = Sum('valor'))

        return Response ({
            'Receita do Mês' : f"R${receita_do_mes}",
            'Despesa do Mês' : f"R${despesa_do_mes}",
            'Saldo final do Mês' : f"R${saldo}",
            'Gasto por categoria' : gasto_por_categoria
        })




