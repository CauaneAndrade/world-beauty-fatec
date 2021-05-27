from datetime import datetime

from django.db.models import Sum
from django.test import TestCase
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto


class TestServicoProdutoCliente(TestCase):
    def setUp(self):
        tel = '12999999999'
        dn1 = datetime(2002, 5, 10)
        dn2 = datetime(2000, 5, 10)
        cliente1 = Cliente.objects.create(nome='teste1', telefone=tel, data_nascimento=dn1, genero='F')
        cliente2 = Cliente.objects.create(nome='teste2', telefone=tel, data_nascimento=dn2, genero='O')
        cliente3 = Cliente.objects.create(nome='teste3', telefone=tel, data_nascimento=dn2, genero='M')

        servico_produto = ServicoProduto.objects.create(
            tipo='S', nome='Corte de cabelo', descricao='corte de todos os tipos'
        )
        servico_produto2 = ServicoProduto.objects.create(
            tipo='S', nome='Unha', descricao='unha de todos os formatos'
        )

        ServicoCliente.objects.create(cliente=cliente1, servico_produto=servico_produto, valor=50)
        ServicoCliente.objects.create(cliente=cliente2, servico_produto=servico_produto, valor=50)
        ServicoCliente.objects.create(cliente=cliente3, servico_produto=servico_produto2, valor=20)

    def test_servico_produto_mais_consumido(self):
        sp_mais_consumido = ServicoCliente.get_servico_produto_mais_consumido()
        self.assertEqual(sp_mais_consumido, 'Corte de cabelo')

    def test_servico_produto_mais_consumido_genero(self):
        genero_masc = 'M'
        sp_mais_consumido = ServicoCliente.get_servico_produto_mais_consumido(genero_masc)
        self.assertEqual(sp_mais_consumido, 'Unha')

    def test_servico_produto_mais_consumido_vazio(self):
        genero_inexistente = 'X'
        sp_mais_consumido = ServicoCliente.get_servico_produto_mais_consumido(genero_inexistente)
        self.assertEqual(sp_mais_consumido, '')
    
    # --------
    
    def test_media_idade_cliente(self):
        media_idade_clientes = Cliente.get_media_idade_clientes()
        self.assertEqual(media_idade_clientes, 20.333333333333332)
    
    def test_media_idade_cliente_genero(self):
        genero_fem = 'F'
        media_idade_clientes = Cliente.get_media_idade_clientes(genero_fem)
        self.assertEqual(media_idade_clientes, 19.0)
    
    def test_media_idade_cliente_genero_vazio(self):
        genero_inexistente = 'X'
        media_idade_clientes = Cliente.get_media_idade_clientes(genero_inexistente)
        self.assertEqual(media_idade_clientes, 0)
