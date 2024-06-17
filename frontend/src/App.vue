<script setup>
import { RouterLink, RouterView } from 'vue-router'

const components = {
  RouterLink,
  RouterView
}

defineExpose(components)
</script>

<template>
  <div class="app-container">
    <RouterView />
  </div>
</template>

<style scoped>
.app-container {
  width: 100%;
  min-height: 100vh; /* Garante que o contêiner ocupe pelo menos a altura total da tela */
  display: flex;
  flex-direction: column;
  align-items: center; /* Alinha os itens ao centro */
}

@media (min-width: 768px) {
  .app-container {
    max-width: 1200px; /* Define um valor máximo para telas maiores */
    margin: 0 auto; /* Centraliza o contêiner na tela */
  }
}
</style>
