from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cidade(request):
        cidade = Cidade.objects.all()
        serializer = CidadeSerializer(cidade, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cidade_id(request, pk):
        cidade = Cidade.objects.get(pk=pk)
        serializer = CidadeSerializer(cidade)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_cidade(request):
        if request.method == 'POST':
            cidade = request.data.get('cidade')

            data = {
                'cod_cidade': request.data.get('cod_cidade'),
                'dcr_cidade': request.data.get('dcr_cidade')
            }

            serializer = CidadeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_cidade(request, pk):
        cidade = Cidade.objects.get(pk=pk)
        serializer = CidadeSerializer(cidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_cidade(request, pk):
        cidade = Cidade.objects.get(pk=pk)
        cidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cliente(request):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cliente_id(request, pk):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_cliente(request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_cliente(request, pk):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_cliente(request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FormaPagtoViewSet(ModelViewSet):
    queryset = FormaPagto.objects.all()
    serializer_class = FormaPagtoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_forma_pagto(request):
        forma_pagto = FormaPagto.objects.all()
        serializer = FormaPagtoSerializer(forma_pagto, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_forma_pagto_id(request, pk):
        forma_pagto = FormaPagto.objects.get(pk=pk)
        serializer = FormaPagtoSerializer(forma_pagto)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_forma_pagto(request):
        serializer = FormaPagtoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_forma_pagto(request, pk):
        forma_pagto = FormaPagto.objects.get(pk=pk)
        serializer = FormaPagtoSerializer(forma_pagto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_forma_pagto(request, pk):
        forma_pagto = FormaPagto.objects.get(pk=pk)
        forma_pagto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_pedido(request, id=None):
        if id:
            pedido = Pedido.objects.get(pk=id)
            serializer = PedidoSerializer(pedido)
            
            consulta = serializer.data
            cliente = Cliente.objects.get(pk=consulta['cod_cliente'])
            consulta['endereco'] = f'{cliente.cod_localidade}, {cliente.cod_bairro}, {cliente.cod_cidade}, {cliente.num_cep}'
            
            itens = ItemPedido.objects.filter(cod_pedido=id)
            produtos = []
            try:
                for i in itens:
                    produtos.append({
                        'nome': Produto.objects.get(pk=i.cod_produto.pk).dcr_produto,
                        'quantidade': i.qtd_produto,
                    })
                consulta['detalhesItens'] = produtos
                
            except Produto.DoesNotExist:
                    print(f"Produto com pk={i.cod_produto.pk} não existe.")

            return Response(consulta)
        
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        consulta = serializer.data

        for p in consulta:
            cliente = Cliente.objects.get(pk=p['cod_cliente'])
            p['endereco'] = f'{cliente.cod_localidade}, {cliente.cod_bairro}, {cliente.cod_cidade}, {cliente.num_cep}'
            itens = ItemPedido.objects.filter(cod_pedido=p['cod_pedido'])
            produtos = []
            for i in itens:
                try:
                    produto = Produto.objects.get(pk=i.cod_produto.pk)
                    produtos.append({
                        'nome': produto.dcr_produto,
                        'quantidade': i.qtd_produto,
                    })
                except Produto.DoesNotExist:
                    print(f"Produto com pk={i.cod_produto.pk} não existe.")
            p['detalhesItens'] = produtos
            #print(produtos, "\n\n")
        return Response(consulta)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_pedido(request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_pedido(request, id=None):
        try:
            pedido = Pedido.objects.get(cod_pedido=id)
            serializer = PedidoSerializer(pedido, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pedido.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_pedido(request, pk):
        pedido = Pedido.objects.get(pk=pk)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_categoria(request):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_categoria_id(request, pk):
        categoria = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_categoria(request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_categoria(request, pk):
        categoria = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_categoria(request, pk):
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_produto(request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_produto_id(request, pk):
        produto = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_produto(request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_produto(request, pk):
        produto = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_produto(request, pk):
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_item_pedido(request):
        item_pedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(item_pedido, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_item_pedido_id(request, pk):
        item_pedido = ItemPedido.objects.get(pk=pk)
        serializer = ItemPedidoSerializer(item_pedido)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_item_pedido(request):
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_item_pedido(request, pk):
        item_pedido = ItemPedido.objects.get(pk=pk)
        serializer = ItemPedidoSerializer(item_pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_item_pedido(request, pk):
        item_pedido = ItemPedido.objects.get(pk=pk)
        item_pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AvaliacaoPedidoViewSet(ModelViewSet):
    queryset = AvaliacaoPedido.objects.all()
    serializer_class = AvaliacaoPedidoSerializer
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_avaliacao_pedido(request):
        avaliacao_pedidos = AvaliacaoPedido.objects.all()
        serializer = AvaliacaoPedidoSerializer(avaliacao_pedidos, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_avaliacao_pedido_id(request, pk):
        avaliacao_pedido = AvaliacaoPedido.objects.get(pk=pk)
        serializer = AvaliacaoPedidoSerializer(avaliacao_pedido)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_avaliacao_pedido(request):
        serializer = AvaliacaoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_avaliacao_pedido(request, pk):
        avaliacao_pedido = AvaliacaoPedido.objects.get(pk=pk)
        serializer = AvaliacaoPedidoSerializer(avaliacao_pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_avaliacao_pedido(request, pk):
        avaliacao_pedido = AvaliacaoPedido.objects.get(pk=pk)
        avaliacao_pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisponibilidadeViewSet(ModelViewSet):
    queryset = Disponibilidade.objects.all()
    serializer_class = DisponibilidadeSerializer
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_disponibilidade(request):
        disponibilidade = Disponibilidade.objects.all()
        serializer = DisponibilidadeSerializer(disponibilidade, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_disponibilidade_id(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        serializer = DisponibilidadeSerializer(disponibilidade)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_disponibilidade(request):
        serializer = DisponibilidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_disponibilidade(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        serializer = DisponibilidadeSerializer(disponibilidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_disponibilidade(request, pk):
        disponibilidade = Disponibilidade.objects.get(pk=pk)
        disponibilidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DisponExcecaoViewSet(ModelViewSet):
    queryset = DisponExcecao.objects.all()
    serializer_class = DisponExcecaoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_dispon_excecao(request):
        dispon_excecao = DisponExcecao.objects.all()
        serializer = DisponExcecaoSerializer(dispon_excecao, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_dispon_excecao_id(request, pk):
        dispon_excecao = DisponExcecao.objects.get(pk=pk)
        serializer = DisponExcecaoSerializer(dispon_excecao)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_dispon_excecao(request):
        serializer = DisponExcecaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_dispon_excecao(request, pk):
        dispon_excecao = DisponExcecao.objects.get(pk=pk)
        serializer = DisponExcecaoSerializer(dispon_excecao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_dispon_excecao(request, pk):
        dispon_excecao = DisponExcecao.objects.get(pk=pk)
        dispon_excecao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EntregaViewSet(ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_entrega(request):
        entrega = Entrega.objects.all()
        serializer = EntregaSerializer(entrega, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_entrega_id(request, pk):
        entrega = Entrega.objects.get(pk=pk)
        serializer = EntregaSerializer(entrega)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_entrega(request):
        serializer = EntregaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_entrega(request, pk):
        entrega = Entrega.objects.get(pk=pk)
        serializer = EntregaSerializer(entrega, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_entrega(request, pk):
        entrega = Entrega.objects.get(pk=pk)
        entrega.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventoViewSet(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_evento(request):
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_evento_id(request, pk):
        evento = Evento.objects.get(pk=pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_evento(request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_evento(request, pk):
        evento = Evento.objects.get(pk=pk)
        serializer = EventoSerializer(evento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_evento(request, pk): 
        evento = Evento.objects.get(pk=pk)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RastreamentoPedidoViewSet(ModelViewSet):
    queryset = RastreamentoPedido.objects.all()
    serializer_class = RastreamentoPedidoSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_rastreamento_pedido(request):
        rastreamento_pedido = RastreamentoPedido.objects.all()
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_rastreamento_pedido_id(request, pk):
        rastreamento_pedido = RastreamentoPedido.objects.get(pk=pk)
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_rastreamento_pedido(request):
        serializer = RastreamentoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_rastreamento_pedido(request, pk):
        rastreamento_pedido = RastreamentoPedido.objects.get(pk=pk)
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_rastreamento_pedido(request, pk):
        rastreamento_pedido = RastreamentoPedido.objects.get(pk=pk)
        rastreamento_pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CardapioViewSet(ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cardapio(request):
        cardapio = Cardapio.objects.all()
        serializer = CardapioSerializer(cardapio, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_cardapio_id(request, pk):
        cardapio = Cardapio.objects.get(pk=pk)
        serializer = CardapioSerializer(cardapio)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_cardapio(request):
        serializer = CardapioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_cardapio(request, pk):
        cardapio = Cardapio.objects.get(pk=pk)
        serializer = CardapioSerializer(cardapio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_cardapio(request, pk):
        cardapio = Cardapio.objects.get(pk=pk)
        cardapio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmprendFuncionarioViewSet(ModelViewSet):
    queryset = EmprendFuncionario.objects.all()
    serializer_class = EmprendFuncionarioSerializer
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_emprend_funcionario(request):
        funcionarios = EmprendFuncionario.objects.all()
        serializer = EmprendFuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_emprend_funcionario_id(request, pk):
        funcionario = EmprendFuncionario.objects.get(pk=pk)
        serializer = EmprendFuncionarioSerializer(funcionario)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_emprend_funcionario(request):
        serializer = EmprendFuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_emprend_funcionario(request, pk):
        funcionario = EmprendFuncionario.objects.get(pk=pk)
        serializer = EmprendFuncionarioSerializer(funcionario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_emprend_funcionario(request, pk):
        funcionario = EmprendFuncionario.objects.get(pk=pk)
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SecaoCardapioViewSet(ModelViewSet):
    queryset = SecaoCardapio.objects.all()
    serializer_class = SecaoCardapioSerializer
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_secao_cardapio(request):
        secao_cardapio = SecaoCardapio.objects.all()
        serializer = SecaoCardapioSerializer(secao_cardapio, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_secao_cardapio_id(request, pk):
        secao_cardapio = SecaoCardapio.objects.get(pk=pk)
        serializer = SecaoCardapioSerializer(secao_cardapio)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_secao_cardapio(request):
        serializer = SecaoCardapioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_secao_cardapio(request, pk):
        secao_cardapio = SecaoCardapio.objects.get(pk=pk)
        serializer = SecaoCardapioSerializer(secao_cardapio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_secao_cardapio(request, pk):
        secao_cardapio = SecaoCardapio.objects.get(pk=pk)
        secao_cardapio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SecaoProdutoViewSet(ModelViewSet):
    queryset = SecaoProduto.objects.all()
    serializer_class = SecaoProdutoSerializer
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_secao_produto(request):
        secao_produto = SecaoProduto.objects.all()
        serializer = SecaoProdutoSerializer(secao_produto, many=True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_secao_produto_id(request, pk):
        secao_produto = SecaoProduto.objects.get(pk=pk)
        serializer = SecaoProdutoSerializer(secao_produto)
        return Response(serializer.data)
    
    @api_view(['POST'])
    #@permission_classes([IsAuthenticated])
    def post_secao_produto(request):
        serializer = SecaoProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['PATCH'])
    #@permission_classes([IsAuthenticated])
    def patch_secao_produto(request, pk):
        secao_produto = SecaoProduto.objects.get(pk=pk)
        serializer = SecaoProdutoSerializer(secao_produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['DELETE'])
    #@permission_classes([IsAuthenticated])
    def delete_secao_produto(request, pk):
        secao_produto = SecaoProduto.objects.get(pk=pk)
        secao_produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)