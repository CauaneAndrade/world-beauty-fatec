from django.db import models


class Servico(models.Model):
    class Tipo(models.TextChoices):
        SERVICO = 'S', ('Serviço')
        PRODUTO = 'P', ('Produto')

    tipo = models.CharField(max_length=1, choices=Tipo.choices)
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    data = models.DateTimeField(auto_now=True)


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


class ServicoCliente(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
