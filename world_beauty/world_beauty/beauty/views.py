from datetime import datetime
from decimal import Decimal

from django.db.models import Avg, ExpressionWrapper, F, fields
from django.views.generic import ListView
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto


class test(ListView):
    queryset = Cliente.objects
    template_name = 'relatorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Cliente.objects.all()
        # genero = request.query_params.get('genero')
        genero = self.request.GET.get('genero')

        if genero and genero in ('F', 'M', 'O'):
            qs = qs.filter(genero=genero)
        idade = ExpressionWrapper(
            (datetime.now().date() - F('data_nascimento')) / 366,
            output_field=fields.IntegerField()
        )
        qs = qs.annotate(idade=idade)
        media_idade = qs.aggregate(Avg('idade'))
        context['media_idade'] = media_idade['idade__avg']
        # ---------------------

        newqs = ServicoCliente.objects.all()
        if genero and genero in ('F', 'M', 'O'):
            newqs = newqs.filter(cliente__genero=genero)
        
        dic = {}
        for i in newqs:
            if i.servico_produto_id in dic.keys():
                dic[i.servico_produto_id] += 1
            elif i.servico_produto_id is not None:
                dic[i.servico_produto_id] = 1
        
        maior = 0
        result = None
        for k, v in dic.items():
            if v > maior:
                maior = v
                result = k
        
        newqs_result = ServicoProduto.objects.filter(id=result)
        context['prod_serv'] = newqs_result.get().nome if newqs_result.exists() else None

        return context
