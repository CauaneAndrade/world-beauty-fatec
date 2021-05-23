from datetime import datetime
from decimal import Decimal

from django.db.models import Avg, Count, ExpressionWrapper, F, fields
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto
from world_beauty.beauty.serializers import (ClienteSerializer,
                                             ServicoClienteSerializer,
                                             ServicoProdutoSerializer)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = Cliente.objects.all().order_by('nome')
        genero = self.request.query_params.get('genero')
        if genero:
            q = q.filter(genero=genero)
        return q


class ServicoClienteViewSet(viewsets.ModelViewSet):
    queryset = ServicoCliente.objects.all().order_by('id')
    serializer_class = ServicoClienteSerializer

    def get_queryset(self):
        q = ServicoCliente.objects.all().order_by('id')
        cliente_id = self.request.query_params.get('cliente_id')
        if cliente_id:
            q = q.filter(cliente__pk=cliente_id)
        return q


class ServicoProdutoViewSet(viewsets.ModelViewSet):
    queryset = ServicoProduto.objects.all()
    serializer_class = ServicoProdutoSerializer


class RelatorioClientesMediaIdadeViewSet(viewsets.ViewSet):
    queryset = Cliente.objects.all()

    def list(self, request):
        qs = Cliente.objects.all()
        genero = request.query_params.get('genero')
        if genero:
            qs = qs.filter(genero=genero)
        idade = ExpressionWrapper(
            (datetime.now().date() - F('data_nascimento')) / Decimal('366'),
            output_field=fields.DateField()
        )
        qs = qs.annotate(idade=idade)
        media_idade = qs.aggregate(Avg('idade'))
        return Response({
            'media_idade': media_idade
        })


class RelatorioServicoViewSet(viewsets.ViewSet):
    queryset = ServicoCliente.objects.all()

    def list(self, request):
        qs = ServicoCliente.objects.all()
        genero = request.query_params.get('genero')
        if genero:
            qs = qs.filter(cliente__genero=genero)
        
        dic = {}
        for i in qs:
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
        
        qs_result = ServicoProduto.objects.filter(id=result)
        maior = qs_result.get().nome if qs_result.exists() else None
        return Response({
            'prod-serv': maior
        })
