<template>
  <div class="main-box">
    <router-view></router-view>
    <GlobalModal />
  </div>
</template>

<script>
import GlobalModal from './components/Modals/GlobalModal.vue';

export default {
  components: {
    GlobalModal,
  },
};
</script>
<style>
.main-box {
  width:100%;
  height:100%;
}
</style>