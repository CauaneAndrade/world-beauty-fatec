from django.db import models


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
        return '%s: %s - %s' % (self.servico_produto.nome, self.cliente.nome, self.data.strftime("%d/%m/%Y"))

