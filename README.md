# IFoodSocial

O IFoodSocial é um projeto inspirado na plataforma iFood, mas voltado para pequenos empreendimentos e cozinheiros independentes. O objetivo é oferecer uma solução acessível para aqueles que desejam vender suas comidas caseiras ou produtos alimentícios sem a necessidade de intermediários grandes e custosos.

## Equipe

Este projeto foi desenvolvido pelo Grupo 3, composto por:

- Arthur Azevedo
- Diego Farias
- Carlos Henrique

## Objetivo do Projeto

O objetivo do IFoodSocial é permitir que pequenos empreendedores e cozinheiros independentes possam gerenciar seus pedidos de maneira eficiente. Inspirado no sistema Kanban, o módulo de gerenciamento de pedidos oferece uma visualização clara e simplificada, onde o usuário pode acompanhar cada etapa do pedido, desde a aceitação/rejeição, passando pela confecção, até a entrega.

## Funcionalidades Principais

- **Aceitação/Rejeição de Pedidos**: Permite que o usuário aceite ou rejeite um pedido.
- **Confecção de Pedidos**: Após aceito, o pedido entra na fase de confecção.
- **Entrega de Pedidos**: O usuário pode marcar o pedido como "saiu para entrega" e acompanhar seu status até a conclusão.

## Configuração Inicial

## Pré-requisitos

- Python 3.6+
- Node.js e npm
- MySQL
- Ambiente Linux/Ubuntu

### Backend (Django)

1. **Crie e ative um ambiente virtual:**

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

2. **Instale as dependências do projeto:**

    ```sh
    pip install -r backend/requirements.txt
    ```

3. **Configuração do banco de dados MySQL:**

    - Instale o MySQL no Ubuntu:

        ```sh
        sudo apt-get update
        sudo apt-get install mysql-server
        ```

    - Inicie o MySQL e acesse o console do MySQL:

        ```sh
        sudo service mysql start
        sudo mysql -u root -p
        ```

    - Crie o banco de dados manualmente:

        ```sql
        SOURCE caminho/para/02C - IFoodSocial - Script DDL - Modelo de Dados.sql;
        SOURCE caminho/para/02D - IFoodSocial - Script DML - Carga de Dados.sql;
        ```

4. **Configure o arquivo de settings do Django:**

    No arquivo `backend/core/settings.py`, configure as informações do banco de dados:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'IFoodSocial',
            'USER': 'seu_usuario_mysql',
            'PASSWORD': 'sua_senha_mysql',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Execute as migrações do banco de dados:**

    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

6. **Inicie o servidor backend:**

    ```sh
    python3 manage.py runserver
    ```

### Frontend (Vue.js)

1. **Acesse a pasta do frontend:**

    ```sh
    cd frontend
    ```

2. **Instale as dependências do projeto:**

    ```sh
    npm install
    ```

3. **Inicie o servidor frontend:**

    ```sh
    npm run dev
    ```

## Conclusão da execução

Após seguir os passos acima, o backend do Django estará rodando em `http://localhost:8000` e o frontend do Vue.js em `xxx`. Certifique-se de que ambos os servidores estejam rodando corretamente para que a aplicação funcione como esperado.

## Modelo de Dados

### Tabelas Essenciais

- **CLIENTE**: Armazena informações sobre os clientes.
- **ENTREGA**: Contém dados sobre as entregas dos pedidos.
- **FORMA_PAGTO**: Define as formas de pagamento aceitas.
- **ITEM_PEDIDO**: Armazena os itens incluídos em cada pedido.
- **PRODUTO**: Informações sobre os produtos disponíveis.
- **PEDIDO**: Principal tabela que armazena todos os pedidos e seus status.
- **BAIRRO, CIDADE, LOCALIDADE**: Conjunto de tabelas que definem o endereço.

### Modificações

Foi adicionada uma variável na tabela de **PEDIDOS** para melhorar o funcionamento do sistema. Além disso, um novo arquivo de população foi criado para melhor demonstrar os testes.

## Explicação das Partes ou Componentes da Solução

### Backend (Django)

O backend é responsável por gerenciar a lógica de negócios e a comunicação com o banco de dados. As principais operações incluem a criação, atualização e deleção de pedidos, bem como a gestão do estado de cada pedido (aceito, em confecção, em entrega).

### Frontend (Vue.js)

O frontend fornece uma interface intuitiva para os usuários gerenciarem seus pedidos. A interface é baseada em um sistema Kanban, permitindo que os usuários vejam facilmente o status de cada pedido e façam atualizações conforme necessário.

## Amostras de Códigos Relevantes

### Exemplo de View para Gerenciar Pedidos no Django

```python
# backend/ifoodsocial/views.py

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
                        'nome': Produto.objects.get(pk=i.cod_item_pedido).dcr_produto,
                        'quantidade': i.qtd_produto,
                })
                consulta['detalhesItens'] = produtos
                
            except Produto.DoesNotExist:
                    print(f"Produto com pk={i.cod_item_pedido} não existe.")

            return Response(consulta)
        
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        consulta = serializer.data

        for p in consulta:
            itens = ItemPedido.objects.filter(cod_pedido=p['cod_pedido'])
            produtos = []
            print(itens, "\n\n")
            for i in itens:
                try:
                    produto = Produto.objects.get(pk=i.cod_item_pedido)
                    produtos.append({
                        'nome': produto.dcr_produto,
                        'quantidade': i.qtd_produto,
                    })
                except Produto.DoesNotExist:
                    print(f"Produto com pk={i.cod_item_pedido} não existe.")
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
```

### Exemplo de Componente Vue para Exibir Pedidos

```vue
<!-- frontend/src/views/PedidosView.vue -->

<template>
  <div>
    <Header @toggleOverlay="toggleOverlay" />
    <div :class="{ 'overlay-active': isOverlayActive }"></div> <!-- Overlay acinzentado -->
    <section class="main">
      <div class="search-bar">
        <input type="text" placeholder="ID do pedido aqui" v-model="searchQuery">
      </div>

      <div class="order-body">
        <div class="order-column" id="analise">
          <h2>Em análise</h2>
          <!-- Assumindo que "analise" é representado por "A" -->
          <div
            class="order-card"
            v-for="order in filteredOrders('A')" 
            :key="order.cod_pedido"
            @click="redirectToDetails(order)"
          >
            <h3>{{ order.cod_pedido }}</h3>
            <p>R${{ order.vlr_pedido }}</p>
            <p>Tipo de pagamento: {{ order.cod_forma_pagto }}</p>
            <p>Data do pedido: {{ order.data_pedido }}</p>
          </div>
        </div>

        <div class="order-column" id="producao">
          <h2>Em produção</h2>
          <!-- Assumindo que "producao" é representado por "P" -->
          <div
            class="order-card"
            v-for="order in filteredOrders('P')" 
            :key="order.cod_pedido"
            @click="redirectToDetails(order)"
          >
            <h3>{{ order.cod_pedido }}</h3>
            <p>Itens do pedido: </p>
            <li v-for="item in order.detalhesItens" :key="item.id">
              {{ item.nome }} - {{ item.quantidade }}x
            </li>
          </div>
        </div>

        <div class="order-column" id="aguardando-entrega">
          <h2>Aguardando entrega</h2>
          <!-- Assumindo que "aguardando" é representado por "E" -->
          <div
            class="order-card"
            v-for="order in filteredOrders('E')" 
            :key="order.cod_pedido"
            @click="redirectToDetails(order)"
          >
            <h3>{{ order.cod_pedido }}</h3>
            <p>Entrega: {{ order.cod_cliente }}</p>
            <p>Data do pedido: {{ order.data_pedido }}</p>
          </div>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import { api } from '../axios-api';

export default {
  name: 'PedidosView',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      apiData: [],
      searchQuery: '',
      isOverlayActive: false,
    };
  },
  created() {
    api.get('/ifoodsocial/getPedido')
      .then(response => {
        this.apiData = response.data;
      })
      .catch(error => {
      });
  },
  methods: {
    filteredOrders(status) {
      if (!this.searchQuery) {
        return this.apiData.filter(order => order.tip_status === status);
      } else {
        // Filtrar pelo ID do pedido
        const query = this.searchQuery.toLowerCase().trim();
        return this.apiData.filter(order => {
          return order.tip_status === status && order.cod_pedido.toString().toLowerCase().includes(query);
        });
      }
    },
    redirectToDetails(order) {
      const { cod_pedido, tip_status } = order;
      let routeName = '';

      switch (tip_status) {
        case 'A':
          routeName = 'DetalhesPedidoAnalise';
          break;
        case 'P':
          routeName = 'DetalhesPedidoProducao';
          break;
        case 'E':
          routeName = 'DetalhesPedidoAguardo';
          break;
        default:
          return;
      }

      this.$router.push({ name: routeName, params: { id: cod_pedido } });
    },
    toggleOverlay(isActive) {
      this.isOverlayActive = isActive; // Atualiza o estado do overlay acinzentado
    }
  }
}
</script>

<style scoped>
.main {
  padding: 20px;
}

.search-bar {
  padding: 15px;
  background-color: #ffffff;
  display: flex;
  justify-content: center;
}

.search-bar input {
  width: 400px;
  padding: 10px;
  background-color: #fff;
  border: 2px solid #aaa8a8;
  border-radius: 10px;
  font-size: 18px;
}

.order-body {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.order-column {
  width: 30%;
  background-color: #f9f9f9;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  height: 60vh;
  position: relative;
  overflow: auto;
}

h2 {
  text-align: center;
}

.order-card {
  background-color: #fff;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 4px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.order-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(239, 80, 0, 0.679);
}

h3 {
  margin: 0;
}

p {
  margin: 5px 0;
}

ul {
  padding-left: 20px;
  margin: 5px 0;
}

li {
  list-style-type: disc;
}

.overlay-active {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); 
  z-index: 999; 
  pointer-events: none; 
}

</style>

```

Esses exemplos demonstram como as principais operações do módulo de gerenciamento de pedidos são implementadas tanto no backend quanto no frontend.