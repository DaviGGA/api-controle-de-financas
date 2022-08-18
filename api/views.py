from rest_framework import viewsets, filters, generics
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny

class ReceitasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as receitas'''
    
    serializer_class = ReceitasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']

    def get_queryset(self):
        return Receita.objects.filter(usuario = self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class DespesasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as despesas'''
    
    serializer_class = DespesasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']


    def get_queryset(self):
        return Despesa.objects.filter(usuario = self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class ListaReceitas(generics.ListAPIView):
    def get_queryset(self):
        
        
        queryset = Receita.objects.filter(data__year = self.kwargs['year'] , data__month = self.kwargs['month'], usuario = self.request.user)
        return queryset
    
    serializer_class = ListagemReceitas


class ListaDespesas(generics.ListAPIView):
    def get_queryset(self):
        queryset = Despesa.objects.filter(data__month = self.kwargs['month'], data__year = self.kwargs['year'], usuario = self.request.user)
        return queryset
    
    serializer_class = ListagemDespesas
    

class ResumoDoMes(APIView):
    queryset = Receita.objects.none()
    
    def get(self, request, mes, ano):
        receita_do_mes = Receita.objects.filter(data__month = mes, data__year = ano,usuario = self.request.user ).aggregate(Sum('valor')) ['valor__sum'] or 0
        despesa_do_mes = Despesa.objects.filter(data__month = mes, data__year = ano,usuario = self.request.user).aggregate(Sum('valor')) ['valor__sum'] or 0
        saldo = receita_do_mes - despesa_do_mes
        gasto_por_categoria = Despesa.objects.filter(data__month = mes, data__year = ano, usuario = self.request.user).values('categoria').annotate(valor_total = Sum('valor'))
        categorias_resumo = ['Alimentação','Saúde','Moradia','Transporte','Educação','Lazer','Imprevistos','Outras']
        gasto_por_categoria_porcento = []
        gasto_por_categoria_individual = 0
        for categoria in categorias_resumo:
            if Despesa.objects.filter(data__month = mes, data__year = ano, categoria = categoria, usuario = self.request.user).aggregate(Sum('valor')) ['valor__sum'] or 0 > 0:
                gasto_por_categoria_individual= Despesa.objects.filter(data__month = mes, data__year = ano, categoria = categoria, usuario = self.request.user).aggregate(Sum('valor')) ['valor__sum'] or 0
                gasto_por_categoria_porcento.append({f'{categoria}' : f'{100*gasto_por_categoria_individual/despesa_do_mes:.2f}%'})


        return Response ({
            'Receita do Mês' : f"R${receita_do_mes}",
            'Despesa do Mês' : f"R${despesa_do_mes}",
            'Saldo final do Mês' : f"R${saldo}",
            'Gasto por categoria' : gasto_por_categoria,
            'Percentual de gasto por categoria' : gasto_por_categoria_porcento
        })


class UsuarioRegistroViewSet(generics.CreateAPIView):
    '''Cria, deleta, atualiza usuários'''
    serializer_class = UsuarioRegistroSerializer
    permission_classes = (AllowAny,)


class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get']
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','email','username']
