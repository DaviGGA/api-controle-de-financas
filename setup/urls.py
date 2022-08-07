from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ReceitasViewset, DespesasViewset

router = routers.DefaultRouter()

router.register('receitas',ReceitasViewset, basename = 'Receitas')
router.register('despesas', DespesasViewset, basename = 'Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
