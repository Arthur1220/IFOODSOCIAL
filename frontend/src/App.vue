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

</style>
