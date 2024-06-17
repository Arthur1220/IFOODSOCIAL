<template>
    <div>
      <main>
        <div class="detalhes-container">
          <button @click="redirectPrevault" class="backdoor"><strong>X</strong></button>
          <header class="header">
            <h1>Pedido N° {{ pedidoId }}</h1>
            <p class="data-pedido">Feito em {{ pedido.data_pedido }}</p>
          </header>
          <p class="status-pagamento">
            <span :class="['status', statusClass]">{{ statusClass }}</span>
          </p>
          <section class="detalhes-pagamento">
            <h2>Detalhes do pagamento</h2>
            <p><strong>Forma de pagamento:</strong> {{ pedido.cod_forma_pagto }}</p>
            <p><strong>Subtotal:</strong> R$ {{ pedido.vlr_pedido }}</p>
          </section>
          <section class="detalhes-entrega">
            <h2>Detalhes da entrega</h2>
            <p><strong>Tipo de entrega:</strong> {{ pedido.endereco }}</p>
            <p><strong>Endereço:</strong> {{ pedido.cod_cliente }}</p>
          </section>
          <h2 class="sub-itens">Itens do pedido</h2>
          <section class="detalhes-itens">
            <ul>
              <li v-for="item in pedido.detalhesItens" :key="item.id">
                {{ item.nome }} - {{ item.quantidade }}x
              </li>
            </ul>
          </section>
          <div class="acoes">
            <button @click="finalizarPedido" class="btn-finalizar">Pedido Enviado</button>
          </div>
        </div>
      </main>
    </div>
  </template>
  
  <script>
  import { api } from '../axios-api';
  
  export default {
    name: 'DetalhesPedidoAnalise',
    props: ['id'],
    data() {
      return {
        pedido: {
          detalhesItens: []
        },
      };
    },
    computed: {
      pedidoId() {
        return this.id;
      },
      statusClass() {
        switch (this.pedido.tip_status) {
        case 'A':
          return 'Análise';
        case 'P':
          return 'Producao';
        case 'E':
          return 'Aguardando';
        case 'F':
          return 'Finalizado';
        default:
          return '';
      }
      }
    },
    created() {
      this.fetchPedidoDetails();
    },
    methods: {
      fetchPedidoDetails() {
        api.get(`/ifoodsocial/getPedido/${this.id}/`)  
          .then(response => {
            this.pedido = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      },
      finalizarPedido() {
        console.log('Pedido finalizado');
        api.patch(`/ifoodsocial/patchPedido/${this.id}/`, { tip_status: 'F' })  
          .then(response => {
            this.pedido.tip_status = 'F'; 
          })
          .catch(error => {
            console.log(error);
          });
      },
      redirectPrevault(){
        this.$router.push({ name: 'Pedidos'});
    }
    },
  };
  </script>
  
  <style scoped>
  p {
    margin-bottom: 5px;
  }

  .detalhes-container {
    width: 400px;
    height: 470px;
    position: absolute;
    top: 52%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 20px;
    border: 1px solid rgba(0, 0, 0, 0.227); 
  }
  
  .header {
    text-align: center;
  }

  .backdoor{
    position: absolute;
    right: 20px;
    background-color: white;
    color: rgb(255, 0, 0);
    border:none;
    font-size:22px;
    font-weight: bolder;
  }

.backdoor:hover{
    transform: scale(1.5);
}
  
  .header h1 {
    font-size: 24px;
    margin: 0;
  }
  
  .header .data-pedido {
    font-size: 14px;
    color: #666;
  }
  
  .detalhes-pagamento, .detalhes-entrega{
    margin-bottom: 20px;
  }
  
  .detalhes-itens {
    margin-bottom: 20px;
    height:100px;
    width: 380px;
    position: relative;
    overflow-y: auto;
  }
  
  .detalhes-pagamento h2, .detalhes-entrega h2, .sub-itens {
    color: #FA6A2E;
    font-size: 20px;
    margin-bottom: 10px;
  }
  
  .sub-itens{
    margin-bottom: 0;
  }
  
  .status-pagamento {
    margin-bottom: 10px;
  }

  .status-pagamento .status {
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: bold;
  }
  
  .status-em-analise {
    background-color: yellow;
    color: black;
  }
  
    .Análise {
    background-color: yellow;
    color: black;
  }

  .Producao {
    background-color: brown;
    color: white;
  }

  .Aguardando {
    background-color: rgb(40, 170, 164);
  }

  .Finalizado {
    background-color: green;
  }
  
  .detalhes-itens li {
    background-color: #f9f9f9;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 5px;
  }
  
  .acoes {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
  }
  
  .acoes .btn-finalizar {
    padding: 15px 30px;
    font-size: 18px;
    background-color: #FA6A2E;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .acoes .btn-finalizar:hover {
    background-color: #e65555;
  }
  </style>
