from django.db import models

class Cidade(models.Model):
    cod_cidade = models.AutoField(primary_key=True)
    dcr_cidade = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.dcr_cidade

    class Meta:
        managed = False
        db_table = 'CIDADE'  # Nome da tabela no banco de dados

class Bairro(models.Model):
    cod_bairro = models.AutoField(primary_key=True)
    dcr_bairro = models.CharField(max_length=45, null=True, blank=True)
    cod_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_column='cod_cidade')

    def __str__(self):
        return self.dcr_bairro

    class Meta:
        managed = False
        db_table = 'BAIRRO'  # Nome da tabela no banco de dados

class Localidade(models.Model):
    cod_localidade = models.AutoField(primary_key=True)
    dcr_localidade = models.CharField(max_length=45, null=True, blank=True)
    cod_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, db_column='cod_bairro')
    localidade_cod_localidade = models.ForeignKey('self', on_delete=models.CASCADE, db_column='localidade_cod_localidade')

    def __str__(self):
        return self.dcr_localidade

    class Meta:
        managed = False
        db_table = 'LOCALIDADE'  # Nome da tabela no banco de dados

class Empreendimento(models.Model):
    cod_empreedimento = models.AutoField(primary_key=True)
    dcr_empreendimento = models.CharField(max_length=45, null=True, blank=True)
    dcr_nome_fantasia = models.CharField(max_length=45, null=True, blank=True)
    dcr_endereco = models.CharField(max_length=45, null=True, blank=True)
    dcr_complemento = models.CharField(max_length=45, null=True, blank=True)
    num_cep = models.CharField(max_length=10, null=True, blank=True)
    cod_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_column='cod_cidade')
    bairro_cod_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, db_column='bairro_cod_bairro')
    cod_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, db_column='cod_localidade')
    img_empreendimento = models.BinaryField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'EMPREENDIMENTO'  # Nome da tabela no banco de dados

class Funcionario(models.Model):
    cod_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=45, null=True, blank=True)
    num_telefone = models.CharField(max_length=15, null=True, blank=True)
    dcr_email = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'FUNCIONARIO'  # Nome da tabela no banco de dados

class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=45, null=True, blank=True)
    dcr_endereco = models.CharField(max_length=45, null=True, blank=True)
    dcr_complemento = models.CharField(max_length=45, null=True, blank=True)
    num_cep = models.CharField(max_length=10, null=True, blank=True)
    cod_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_column='cod_cidade')
    cod_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, db_column='cod_bairro')
    cod_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, db_column='cod_localidade')

    class Meta:
        managed = False
        db_table = 'CLIENTE'  # Nome da tabela no banco de dados

class FormaPagto(models.Model):
    cod_forma_pagto = models.AutoField(primary_key=True)
    dcr_forma_pagto = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.dcr_forma_pagto
    
    class Meta:
        managed = False
        db_table = 'FORMA_PAGTO'  # Nome da tabela no banco de dados

class Pedido(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    tip_pedido = models.CharField(max_length=1, null=True, blank=True)
    data_pedido = models.DateTimeField(null=True, blank=True)
    vlr_pedido = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    tip_status = models.CharField(max_length=1, null=True, blank=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cod_cliente')
    cod_forma_pagto = models.ForeignKey(FormaPagto, on_delete=models.CASCADE, null=True, blank=True, db_column='cod_forma_pagto')
    dcr_dados_pagto = models.CharField(max_length=200, null=True, blank=True)

    
    class Meta:
        managed = False
        db_table = 'PEDIDO'  # Nome da tabela no banco de dados

class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    dcr_categoria = models.CharField(max_length=45, null=True, blank=True)
    img_categoria = models.BinaryField(null=True, blank=True)
    cod_empreedimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreedimento')

    class Meta:
        managed = False
        db_table = 'CATEGORIA'  # Nome da tabela no banco de dados

class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    dcr_produto = models.CharField(max_length=45, null=True, blank=True)
    img_produto = models.BinaryField(null=True, blank=True)
    vlr_produto = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    flag_disponivel = models.CharField(max_length=1, null=True, blank=True)
    cod_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column='cod_categoria')
    cod_empreedimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreedimento')

    def __str__(self):
        return self.dcr_produto
    
    class Meta:
        managed = False
        db_table = 'PRODUTO'  # Nome da tabela no banco de dados

class ItemPedido(models.Model):
    cod_item_pedido = models.AutoField(primary_key=True)
    vlr_produto = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    qtd_produto = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    vlr_total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='cod_pedido')
    cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column='cod_produto')

    class Meta:
        managed = False
        db_table = 'ITEM_PEDIDO'  # Nome da tabela no banco de dados

class AvaliacaoPedido(models.Model):
    cod_avaliacao_pedido = models.AutoField(primary_key=True)
    num_nota_avaliacao = models.IntegerField(null=True, blank=True)
    txt_avaliacao = models.CharField(max_length=100, null=True, blank=True)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='cod_pedido')
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cod_cliente')

    class Meta:
        managed = False
        db_table = 'AVALIACAO_PEDIDO'  # Nome da tabela no banco de dados

class Disponibilidade(models.Model):
    cod_disponibilidade = models.AutoField(primary_key=True)
    num_dia_semana = models.IntegerField(null=True, blank=True)
    hora_fim = models.DateTimeField(null=True, blank=True)
    hora_inicio = models.DateTimeField(null=True, blank=True)
    cod_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, db_column='cod_localidade')
    cod_empreedimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreedimento')

    class Meta:
        managed = False
        db_table = 'DISPONIBILIDADE'  # Nome da tabela no banco de dados

class DisponExcecao(models.Model):
    cod_dispon_excecao = models.AutoField(primary_key=True)
    data_excecao = models.DateTimeField(null=True, blank=True)
    tip_excecao = models.CharField(max_length=1, null=True, blank=True)
    hora_inicio = models.DateTimeField(null=True, blank=True)
    hora_fim = models.DateTimeField(null=True, blank=True)
    cod_empreedimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreedimento')
    cod_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, db_column='cod_localidade')

    class Meta:
        managed = False
        db_table = 'DISPON_EXCECAO'  # Nome da tabela no banco de dados

class Entrega(models.Model):
    cod_entrega = models.AutoField(primary_key=True)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='cod_pedido')
    cod_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='cod_funcionario')
    data_saida = models.DateTimeField(null=True, blank=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
    vlr_entrega = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    dcr_endereco = models.CharField(max_length=45, null=True, blank=True)
    dcr_complem = models.CharField(max_length=45, null=True, blank=True)
    num_cep = models.CharField(max_length=10, null=True, blank=True)
    txt_referencia = models.CharField(max_length=45, null=True, blank=True)
    cod_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_column='cod_cidade')
    cod_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, db_column='cod_bairro')
    cod_localidade = models.ForeignKey(Localidade, on_delete=models.CASCADE, db_column='cod_localidade')
    flag_encomenda = models.CharField(max_length=1, null=True, blank=True)
    flag_entregador = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ENTREGA'  # Nome da tabela no banco de dados

class Evento(models.Model):
    cod_evento = models.AutoField(primary_key=True)
    dcr_evento = models.CharField(max_length=45, null=True, blank=True)
    num_ordem_evento = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'EVENTO'  # Nome da tabela no banco de dados

class RastreamentoPedido(models.Model):
    cod_rastreamento_pedido = models.AutoField(primary_key=True)
    cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='cod_pedido')
    cod_evento_pedido = models.ForeignKey(Evento, on_delete=models.CASCADE, db_column='cod_evento_pedido')
    data_hora_evento = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'RASTREAMENTO_PEDIDO'  # Nome da tabela no banco de dados

class Cardapio(models.Model):
    cod_cardapio = models.AutoField(primary_key=True)
    dcr_cardapio = models.CharField(max_length=45, blank=True, null=True)
    dcr_titulo_apres = models.CharField(max_length=45, blank=True, null=True)
    cod_empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreendimento')

    class Meta:
        managed = False
        db_table = 'CARDAPIO'  # Nome da tabela no banco de dados

class EmprendFuncionario(models.Model):
    cod_emprend_funcionario = models.AutoField(primary_key=True)
    tip_funcionario = models.CharField(max_length=1, blank=True, null=True)
    cod_empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE, db_column='cod_empreendimento')
    cod_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='cod_funcionario')
    img_emprend_funcionario = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPREEND_FUNCIONARIO'  # Nome da tabela no banco de dados

class SecaoCardapio(models.Model):
    cod_secao_cardapio = models.AutoField(primary_key=True)
    dcr_secao_cardapio = models.CharField(max_length=45, blank=True, null=True)
    dcr_titulo_apres = models.CharField(max_length=45, blank=True, null=True)
    cod_cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE, db_column='cod_cardapio')
    num_ordem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SECAO_CARDAPIO'  # Nome da tabela no banco de dados

class SecaoProduto(models.Model):
    cod_secao_produto = models.CharField(max_length=45, primary_key=True)
    produto_cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column='produto_cod_produto')
    secao_cardapio_cod_secao_cardapio = models.ForeignKey(SecaoCardapio, on_delete=models.CASCADE, db_column='secao_cardapio_cod_secao_cardapio')
    num_ordem = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SECAO_PRODUTOS'  # Nome da tabela no banco de dados