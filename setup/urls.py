from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ReceitasViewset, DespesasViewset, ListaReceitas, ListaDespesas, ResumoDoMes

router = routers.DefaultRouter()

router.register('receitas',ReceitasViewset, basename = 'Receitas')
router.register('despesas', DespesasViewset, basename = 'Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:month>/<int:year>',ListaReceitas.as_view()),
    path('despesas/<int:month>/<int:year>',ListaDespesas.as_view()),
    path('resumo/<int:mes>/<int:ano>', ResumoDoMes.as_view())
]
