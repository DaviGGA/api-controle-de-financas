from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Financeira",
      default_version='v1',
      description="Registro de Receitas e Despesas",
      terms_of_service="#",
      contact=openapi.Contact(email="davigregorio.a@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register('receitas',ReceitasViewset, basename = 'Receitas')
router.register('despesas', DespesasViewset, basename = 'Despesas')
router.register('usuarios', UsuarioViewSet, basename = 'Usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('receitas/<int:month>/<int:year>',ListaReceitas.as_view()),
    path('despesas/<int:month>/<int:year>',ListaDespesas.as_view()),
    path('resumo/<int:mes>/<int:ano>', ResumoDoMes.as_view()),
    path('registro/',UsuarioRegistroViewSet.as_view()),
    path('documentacao/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   

]
