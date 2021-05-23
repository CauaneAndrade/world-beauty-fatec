from rest_framework import serializers
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'telefone', 'data_nascimento', 'genero', 'data_cadastro']


class ServicoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoProduto
        fields = ['id', 'tipo', 'nome', 'descricao']


class ServicoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoCliente
        fields = ['id', 'cliente', 'servico_produto', 'valor', 'data']
