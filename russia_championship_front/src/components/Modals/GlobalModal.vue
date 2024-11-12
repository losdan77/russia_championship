<template>
  <div v-show="isVisible" class="modal-overlay" @click="closeModal">
    <div class="modal-content" :class="{ 'slide-down': isVisible }">
      <p>{{ message }}</p>
    </div>
  </div>
</template>

<script>
import eventBus from '../../eventBus';

export default {
  data() {
    return {
      isVisible: false,
      message: '',
    };
  },
  created() {
    // Подписываемся на событие "show-modal" через eventBus
    eventBus.on('show-modal', this.showModal);
  },
  methods: {
    showModal(message) {
      this.message = message;
      this.isVisible = true;

      // Закрываем модальное окно через 2 секунды
      setTimeout(() => {
        this.isVisible = false;
      }, 2000);
    },
    closeModal() {
      this.isVisible = false;
    },
  },
  beforeUnmount() {
    // Отписываемся от события, чтобы избежать утечек памяти
    eventBus.off('show-modal', this.showModal);
  },
};
</script>

<style>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: start;
  background: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fff;
  padding: 20px 30px;
  border-radius: 8px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
  pointer-events: auto; 
  opacity: 0;
  transform: translateY(-50px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.slide-down {
  opacity: 1;
  transform: translateY(20px);
}
</style>
