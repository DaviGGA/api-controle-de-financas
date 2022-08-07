from rest_framework import viewsets, generics
from .models import Receita, Despesa
from .serializer import ReceitasSerializer, DespesasSerializer

class ReceitasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as receitas'''
    queryset = Receita.objects.all()
    serializer_class = ReceitasSerializer

class DespesasViewset(viewsets.ModelViewSet):
    '''Exibindo todas as despesas'''
    queryset = Despesa.objects.all()
    serializer_class = DespesasSerializer





