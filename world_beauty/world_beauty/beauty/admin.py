from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from world_beauty.beauty import views
from world_beauty.beauty.models import Cliente, ServicoCliente, ServicoProduto

admin.site.unregister(Group)

class ClienteFilter(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'data_nascimento', 'genero', 'view_data_cadastro', 'view_services_link']
    list_filter = ['genero', 'nome']

    def view_data_cadastro(self, obj):
        return obj.data_cadastro.strftime("%d/%m/%Y")

    def view_services_link(self, obj):
        li = ''
        for i in obj.servicocliente_set.all():
            li += f'<li>{i.servico_produto.nome}</li>'
        return format_html(f'<ul>{li}</ul>')

    view_services_link.short_description = "Serviços/Produtos"
    view_data_cadastro.short_description = "Data cadastro"


class ServicoClienteFilter(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'servico_produto', 'data', 'valor']
    list_filter = ['cliente',]

admin.site.register(Cliente, ClienteFilter)
admin.site.register(ServicoCliente, ServicoClienteFilter)
admin.site.register(ServicoProduto)
