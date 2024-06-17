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
            <p>R$ {{ order.vlr_pedido }}</p>
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
            <p>Entrega: {{ order.endereco }}</p>
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
      this.isOverlayActive = isActive;
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
  background-color: #ececec;
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
