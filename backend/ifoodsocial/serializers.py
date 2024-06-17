from django import db
from rest_framework import serializers
from .models import *

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'CIDADE'
        model = Cidade
        fields = '__all__'

class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'BAIRRO'
        model = Bairro
        fields = '__all__'

class LocalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'LOCALIDADE'
        model = Localidade
        fields = '__all__'

class EmpreendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'EMPREENDIMENTO'
        model = Empreendimento
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'FUNCIONARIO'
        model = Funcionario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'CLIENTE'
        model = Cliente
        fields = '__all__'

class FormaPagtoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'FORMA_PAGTO'
        model = FormaPagto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    data_pedido = serializers.DateTimeField(format="%d/%m/%Y | %H:%Mh", required=False, allow_null=True)    
    cod_forma_pagto = serializers.StringRelatedField()
    
    class Meta:
        db_table = 'PEDIDO'
        model = Pedido
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'CATEGORIA'
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'PRODUTO'
        model = Produto
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'ITEM_PEDIDO'
        model = ItemPedido
        fields = '__all__'

class AvaliacaoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'AVALIACAO_PEDIDO'
        model = AvaliacaoPedido
        fields = '__all__'

class DisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'DISPONIBILIDADE'
        model = Disponibilidade
        fields = '__all__'

class DisponExcecaoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'DISPON_EXCECAO'
        model = DisponExcecao
        fields = '__all__'

class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'ENTREGA'
        model = Entrega
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'EVENTO'
        model = Evento
        fields = '__all__'

class RastreamentoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'RASTREAMENTO_PEDIDO'
        model = RastreamentoPedido
        fields = '__all__'

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'CARDAPIO'
        model = Cardapio
        fields = '__all__'

class EmprendFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'EMPREND_FUNCIONARIO'
        model = EmprendFuncionario
        fields = '__all__'

class SecaoCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'SECAO_CARDAPIO'
        model = SecaoCardapio
        fields = '__all__'

class SecaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'SECAO_PRODUTO'
        model = SecaoProduto
        fields = '__all__'