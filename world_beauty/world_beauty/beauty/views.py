from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, ExpressionWrapper, F, fields
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto


@method_decorator(login_required(login_url='/admin/'), name='dispatch')
class RelatorioView(ListView):
    queryset = Cliente.objects
    template_name = 'relatorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genero = self.request.GET.get('genero')
        context['media_idade'] = Cliente.get_media_idade_clientes(genero)
        context['prod_serv'] = ServicoCliente.get_servico_produto_mais_consumido(genero)
        return context
