from django.urls import path
from .views import CidadeViewSet, ClienteViewSet, FormaPagtoViewSet, PedidoViewSet, CategoriaViewSet, ProdutoViewSet, ItemPedidoViewSet, AvaliacaoPedidoViewSet, DisponibilidadeViewSet, DisponExcecaoViewSet, EntregaViewSet, EventoViewSet, RastreamentoPedidoViewSet, CardapioViewSet, EmprendFuncionarioViewSet, SecaoCardapioViewSet, SecaoProdutoViewSet

urlpatterns = [
    path('getCidade', CidadeViewSet.get_cidade, name='getCidade'),
    path('getCidadeID/<int:id>/', CidadeViewSet.get_cidade_id, name='getCidadeID'),
    path('postCidade', CidadeViewSet.post_cidade, name='postCidade'),
    path('patchCidade/<int:id>/', CidadeViewSet.patch_cidade, name='patchCidade'),
    path('deleteCidade/<int:id>/', CidadeViewSet.delete_cidade, name='deleteCidade'),

    path('getCliente', ClienteViewSet.get_cliente, name='getCliente'),
    path('getClienteID/<int:id>/', ClienteViewSet.get_cliente_id, name='getClienteID'),
    path('postCliente', ClienteViewSet.post_cliente, name='postCliente'),
    path('patchCliente/<int:id>/', ClienteViewSet.patch_cliente, name='patchCliente'),
    path('deleteCliente/<int:id>/', ClienteViewSet.delete_cliente, name='deleteCliente'),

    path('getFormaPagto', FormaPagtoViewSet.get_forma_pagto, name='getFormaPagto'),
    path('getFormaPagtoID/<int:id>/', FormaPagtoViewSet.get_forma_pagto_id, name='getFormaPagtoID'),
    path('postFormaPagto', FormaPagtoViewSet.post_forma_pagto, name='postFormaPagto'),
    path('patchFormaPagto/<int:id>/', FormaPagtoViewSet.patch_forma_pagto, name='patchFormaPagto'),
    path('deleteFormaPagto/<int:id>/', FormaPagtoViewSet.delete_forma_pagto, name='deleteFormaPagto'),

    path('getPedido', PedidoViewSet.get_pedido, name='getPedido'),
    path('getPedido/<int:id>/', PedidoViewSet.get_pedido, name='getPedidoID'),
    path('postPedido', PedidoViewSet.post_pedido, name='postPedido'),
    path('patchPedido/<int:id>/', PedidoViewSet.patch_pedido, name='patchPedido'),
    path('deletePedido/<int:id>/', PedidoViewSet.delete_pedido, name='deletePedido'),

    path('getCategoria', CategoriaViewSet.get_categoria, name='getCategoria'),
    path('getCategoriaID/<int:id>/', CategoriaViewSet.get_categoria_id, name='getCategoriaID'),
    path('postCategoria', CategoriaViewSet.post_categoria, name='postCategoria'),
    path('patchCategoria/<int:id>/', CategoriaViewSet.patch_categoria, name='patchCategoria'),
    path('deleteCategoria/<int:id>/', CategoriaViewSet.delete_categoria, name='deleteCategoria'),

    path('getProduto', ProdutoViewSet.get_produto, name='getProduto'),
    path('getProdutoID/<int:id>/', ProdutoViewSet.get_produto_id, name='getProdutoID'),
    path('postProduto', ProdutoViewSet.post_produto, name='postProduto'),
    path('patchProduto/<int:id>/', ProdutoViewSet.patch_produto, name='patchProduto'),
    path('deleteProduto/<int:id>/', ProdutoViewSet.delete_produto, name='deleteProduto'),

    path('getItemPedido', ItemPedidoViewSet.get_item_pedido, name='getItemPedido'),
    path('getItemPedidoID/<int:id>/', ItemPedidoViewSet.get_item_pedido_id, name='getItemPedidoID'),
    path('postItemPedido', ItemPedidoViewSet.post_item_pedido, name='postItemPedido'),
    path('patchItemPedido/<int:id>/', ItemPedidoViewSet.patch_item_pedido, name='patchItemPedido'),
    path('deleteItemPedido/<int:id>/', ItemPedidoViewSet.delete_item_pedido, name='deleteItemPedido'),

    path('getAvaliacaoPedido', AvaliacaoPedidoViewSet.get_avaliacao_pedido, name='getAvaliacaoPedido'),
    path('getAvaliacaoPedidoID/<int:id>/', AvaliacaoPedidoViewSet.get_avaliacao_pedido_id, name='getAvaliacaoPedidoID'),
    path('postAvaliacaoPedido', AvaliacaoPedidoViewSet.post_avaliacao_pedido, name='postAvaliacaoPedido'),
    path('patchAvaliacaoPedido/<int:id>/', AvaliacaoPedidoViewSet.patch_avaliacao_pedido, name='patchAvaliacaoPedido'),
    path('deleteAvaliacaoPedido/<int:id>/', AvaliacaoPedidoViewSet.delete_avaliacao_pedido, name='deleteAvaliacaoPedido'),

    path('getDisponibilidade', DisponibilidadeViewSet.get_disponibilidade, name='getDisponibilidade'),
    path('getDisponibilidadeID/<int:id>/', DisponibilidadeViewSet.get_disponibilidade_id, name='getDisponibilidadeID'),
    path('postDisponibilidade', DisponibilidadeViewSet.post_disponibilidade, name='postDisponibilidade'),
    path('patchDisponibilidade/<int:id>/', DisponibilidadeViewSet.patch_disponibilidade, name='patchDisponibilidade'),
    path('deleteDisponibilidade/<int:id>/', DisponibilidadeViewSet.delete_disponibilidade, name='deleteDisponibilidade'),

    path('getDisponExcecao', DisponExcecaoViewSet.get_dispon_excecao, name='getDisponExcecao'),
    path('getDisponExcecaoID/<int:id>/', DisponExcecaoViewSet.get_dispon_excecao_id, name='getDisponExcecaoID'),
    path('postDisponExcecao', DisponExcecaoViewSet.post_dispon_excecao, name='postDisponExcecao'),
    path('patchDisponExcecao/<int:id>/', DisponExcecaoViewSet.patch_dispon_excecao, name='patchDisponExcecao'),
    path('deleteDisponExcecao/<int:id>/', DisponExcecaoViewSet.delete_dispon_excecao, name='deleteDisponExcecao'),

    path('getEntrega', EntregaViewSet.get_entrega, name='getEntrega'),
    path('getEntregaID/<int:id>/', EntregaViewSet.get_entrega_id, name='getEntregaID'),
    path('postEntrega', EntregaViewSet.post_entrega, name='postEntrega'),
    path('patchEntrega/<int:id>/', EntregaViewSet.patch_entrega, name='patchEntrega'),
    path('deleteEntrega/<int:id>/', EntregaViewSet.delete_entrega, name='deleteEntrega'),

    path('getEvento', EventoViewSet.get_evento, name='getEvento'),
    path('getEventoID/<int:id>/', EventoViewSet.get_evento_id, name='getEventoID'),
    path('postEvento', EventoViewSet.post_evento, name='postEvento'),
    path('patchEvento/<int:id>/', EventoViewSet.patch_evento, name='patchEvento'),
    path('deleteEvento/<int:id>/', EventoViewSet.delete_evento, name='deleteEvento'),

    path('getRastreamentoPedido', RastreamentoPedidoViewSet.get_rastreamento_pedido, name='getRastreamentoPedido'),
    path('getRastreamentoPedidoID/<int:id>/', RastreamentoPedidoViewSet.get_rastreamento_pedido_id, name='getRastreamentoPedidoID'),
    path('postRastreamentoPedido', RastreamentoPedidoViewSet.post_rastreamento_pedido, name='postRastreamentoPedido'),
    path('patchRastreamentoPedido/<int:id>/', RastreamentoPedidoViewSet.patch_rastreamento_pedido, name='patchRastreamentoPedido'),
    path('deleteRastreamentoPedido/<int:id>/', RastreamentoPedidoViewSet.delete_rastreamento_pedido, name='deleteRastreamentoPedido'),

    path('getCardapio', CardapioViewSet.get_cardapio, name='getCardapio'),
    path('getCardapioID/<int:id>/', CardapioViewSet.get_cardapio_id, name='getCardapioID'),
    path('postCardapio', CardapioViewSet.post_cardapio, name='postCardapio'),
    path('patchCardapio/<int:id>/', CardapioViewSet.patch_cardapio, name='patchCardapio'),
    path('deleteCardapio/<int:id>/', CardapioViewSet.delete_cardapio, name='deleteCardapio'),

    path('getEmprendFuncionario', EmprendFuncionarioViewSet.get_emprend_funcionario, name='getEmprendFuncionario'),
    path('getEmprendFuncionarioID/<int:id>/', EmprendFuncionarioViewSet.get_emprend_funcionario_id, name='getEmprendFuncionarioID'),
    path('postEmprendFuncionario', EmprendFuncionarioViewSet.post_emprend_funcionario, name='postEmprendFuncionario'),
    path('patchEmprendFuncionario/<int:id>/', EmprendFuncionarioViewSet.patch_emprend_funcionario, name='patchEmprendFuncionario'),
    path('deleteEmprendFuncionario/<int:id>/', EmprendFuncionarioViewSet.delete_emprend_funcionario, name='deleteEmprendFuncionario'),

    path('getSecaoCardapio', SecaoCardapioViewSet.get_secao_cardapio, name='getSecaoCardapio'),
    path('getSecaoCardapioID/<int:id>/', SecaoCardapioViewSet.get_secao_cardapio_id, name='getSecaoCardapioID'),
    path('postSecaoCardapio', SecaoCardapioViewSet.post_secao_cardapio, name='postSecaoCardapio'),
    path('patchSecaoCardapio/<int:id>/', SecaoCardapioViewSet.patch_secao_cardapio, name='patchSecaoCardapio'),
    path('deleteSecaoCardapio/<int:id>/', SecaoCardapioViewSet.delete_secao_cardapio, name='deleteSecaoCardapio'),

    path('getSecaoProduto', SecaoProdutoViewSet.get_secao_produto, name='getSecaoProduto'),
    path('getSecaoProdutoID/<int:id>/', SecaoProdutoViewSet.get_secao_produto_id, name='getSecaoProdutoID'),
    path('postSecaoProduto', SecaoProdutoViewSet.post_secao_produto, name='postSecaoProduto'),
    path('patchSecaoProduto/<int:id>/', SecaoProdutoViewSet.patch_secao_produto, name='patchSecaoProduto'),
    path('deleteSecaoProduto/<int:id>/', SecaoProdutoViewSet.delete_secao_produto, name='deleteSecaoProduto')
]