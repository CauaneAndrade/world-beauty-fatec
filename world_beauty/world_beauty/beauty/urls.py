from django.urls import include, path
from rest_framework import routers
from world_beauty.beauty import views, viewsets

router = routers.DefaultRouter()
router.register(r'clientes', viewsets.ClienteViewSet)
router.register(r'servicos-cliente', viewsets.ServicoClienteViewSet)
router.register(r'servicos-produto', viewsets.ServicoProdutoViewSet)
router.register(r'relatorio-media-idade', viewsets.RelatorioClientesMediaIdadeViewSet)
router.register(r'relatorio-servico', viewsets.RelatorioServicoViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.test.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
