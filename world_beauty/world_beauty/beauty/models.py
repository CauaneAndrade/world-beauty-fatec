from datetime import datetime

from django.db import models
from django.db.models import Avg, ExpressionWrapper, F, fields


class Cliente(models.Model):
    class Genero(models.TextChoices):
        FEMININO = 'F', ('Feminino')
        MASCULINO = 'M', ('Masculino')
        OUTRO = 'O', ('Outro')

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=2, choices=Genero.choices)
    data_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome} - {self.id}'
    
    @classmethod
    def get_cliente_qs(cls, genero=None):
        c_qs = cls.objects.all()
        if genero and genero not in ('F', 'M', 'O'):
            c_qs = c_qs.none()
        elif genero:
            c_qs = c_qs.filter(genero=genero)
        return c_qs

    @classmethod
    def get_media_idade_clientes(cls, genero=None) -> float:
        qs = cls.get_cliente_qs(genero)

        idade_em_dias = datetime.now().date() - F('data_nascimento')
        idade_wrapper = ExpressionWrapper(
            idade_em_dias / 366, output_field=fields.IntegerField()
        )
        qs = qs.annotate(idade=idade_wrapper)
        return qs.aggregate(Avg('idade'))['idade__avg'] or 0


class ServicoProduto(models.Model):
    class Tipo(models.TextChoices):
        SERVICO = 'S', ('Serviço')
        PRODUTO = 'P', ('Produto')

    tipo = models.CharField(max_length=1, choices=Tipo.choices, default=Tipo.SERVICO)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.nome


class ServicoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    servico_produto = models.ForeignKey(ServicoProduto, on_delete=models.DO_NOTHING, null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.servico_produto.nome}: {self.cliente.nome} - {self.data.strftime("%d/%m/%Y")}'

    @classmethod
    def get_servico_produto_qs(cls, genero=None):
        sp_qs = cls.objects.all()
        if genero and genero not in ('F', 'M', 'O'):
            sp_qs = sp_qs.none()
        elif genero:
            sp_qs = sp_qs.filter(cliente__genero=genero)
        return sp_qs

    @classmethod
    def get_servico_produto_mais_consumido(cls, genero=None) -> str:
        qs = cls.get_servico_produto_qs(genero)
        dic = {}
        for i in qs:
            sp_id = i.servico_produto_id
            if sp_id in dic.keys():
                dic[sp_id] += 1
            elif sp_id is not None:
                dic[sp_id] = 1
        
        maior = 0
        pk_sp = None
        for k, v in dic.items():
            if v > maior:
                maior = v
                pk_sp = k
        
        sp_qs = ServicoProduto.objects.filter(id=pk_sp)
        return sp_qs.get().nome if sp_qs.exists() else ''
