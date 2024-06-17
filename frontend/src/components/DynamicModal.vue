<template>
    <div v-if="isVisible" class="modal-overlay">
      <div class="modal-container">
        <button class="close-button" @click="closeModal">x</button>
        <div class="modal-content" v-html="content"></div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watchEffect } from 'vue';
  
  const props = defineProps({
    isVisible: Boolean,
    url: String
  });
  
  const emit = defineEmits(['close']);
  
  const content = ref('');
  
  const closeModal = () => {
    emit('close');
  };
  
  watchEffect(() => {
    if (props.isVisible && props.url) {
      fetch(props.url)
        .then(response => response.text())
        .then(data => {
          content.value = data;
        })
        .catch(error => {
          console.error('Error loading content:', error);
        });
    }
  });
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-container {
    background: white;
    padding: 20px;
    border-radius: 8px;
    position: relative;
    max-width: 90%;
    width: 80%;
    height: 80%;
    overflow: auto;
  }
  
  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
  }
  
  .modal-content {
    padding: 20px;
  }
  </style>
  