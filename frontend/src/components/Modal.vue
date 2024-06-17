<template>
    <div class="modal-overlay" v-if="isVisible">
      <div class="modal-container">
        <button class="close-button" @click="closeModal">x</button>
        <div class="modal-content">
          <slot></slot>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue';
  
  const props = defineProps({
    isVisible: {
      type: Boolean,
      default: false,
    }
  });
  
  const closeModal = () => {
    // Emit an event to close the modal
    emit('close');
  };
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
    max-width: 500px;
    width: 100%;
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
  