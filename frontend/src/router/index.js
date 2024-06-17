import { createRouter, createWebHistory } from 'vue-router'
import PedidosView from '@/views/PedidosView.vue';
import DetalhesPedidoAnalise from '@/views/DetalhesPedidoAnalise.vue';
import DetalhesPedidoProducao from '@/views/DetalhesPedidoProducao.vue';
import DetalhesPedidoAguardo from '@/views/DetalhesPedidoAguardo.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Pedidos',
      component: PedidosView,
    },
    {
      path: '/detalhes/analise/:id',
      name: 'DetalhesPedidoAnalise',
      component: DetalhesPedidoAnalise,
      props: true,
    },
    {
      path: '/detalhes/producao/:id',
      name: 'DetalhesPedidoProducao',
      component: DetalhesPedidoProducao,
      props: true,
    },
    {
      path: '/detalhes/aguardo/:id',
      name: 'DetalhesPedidoAguardo',
      component: DetalhesPedidoAguardo,
      props: true,
    },
  ]
})

export default router
