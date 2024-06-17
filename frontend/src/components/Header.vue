<template>
  <header class="header">
    <img src="@/assets/logo.svg" alt="Logo" class="logo">
    <h1>Gestão de Pedidos</h1>
    <div class="status-box">
      <button @click="toggleText" :style="{ color: textColor, backgroundColor: buttonBackgroundColor }">{{ buttonText }}</button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      buttonText: 'Aberto',
      textColor: '#188300f5',
      buttonBackgroundColor: 'white', 
      isClosed: false, 
    };
  },
  methods: {
    toggleText() {
      this.isClosed = !this.isClosed; // Alternar entre fechado e aberto
      if (this.isClosed) {
        this.buttonText = 'Fechado';
        this.textColor = '#f00';
        this.buttonBackgroundColor = 'white'; // Cor de fundo transparente para o botão
        this.$emit('toggleOverlay', true); // Emitir evento para ativar o overlay acinzentado
      } else {
        this.buttonText = 'Aberto';
        this.textColor = '#188300f5';
        this.buttonBackgroundColor = 'white'; // Cor de fundo do botão para branco
        this.$emit('toggleOverlay', false); // Emitir evento para desativar o overlay acinzentado
      }
    },
  },
};
</script>

<style scoped>
.header {
  background-color: #FA6A2E;
  color: #fff;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  width: 50px;
  height: auto;
}

.header h1 {
  flex-grow: 1;
  text-align: center;
  margin: 0;
}

.status-box button {
  margin: 0;
  font-size: 15px;
  font-weight: bold;
  padding: 10px;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 50px;
  border-radius: 10px;
  cursor: pointer;
}

.status-box button:hover {
  background-color: rgba(255, 255, 255, 0.4);
}
</style>
