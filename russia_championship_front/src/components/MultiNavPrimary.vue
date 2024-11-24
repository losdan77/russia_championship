<template>
    <div class="container">
      <div class="button-row">
        <button 
          v-for="(tab, index) in tabs" 
          :key="index" 
          :class="{ active: activeTab === index }"
          @click="setActiveTab(index)"
        >
          {{ tab.label }}
        </button>
      </div>
      
      <div class="content-block">
        <component :is="tabs[activeTab].component"></component>
      </div>
    </div>
  </template>
  
  <script>
    import CalendarPrymaryComp from '../components/CalendarPrymaryComp.vue';
    import BrassComp from './BrassComp.vue';
    import NewsComp from './NewsComp.vue';
    import UpdateComp from './UpdateComp.vue';
  import { shallowRef } from 'vue';
  export default {
    data() {
      return {
        components: {
            CalendarPrymaryComp,
            BrassComp,
            NewsComp

        },
        activeTab: 0,
        tabs: [
          { label: 'Календарь событий', component: shallowRef(CalendarPrymaryComp) },
          { label: 'Новости спорта', component: shallowRef(NewsComp)},
          { label: 'Министерство', component: shallowRef(BrassComp) },
          { label: 'Обновления', component: shallowRef(UpdateComp) },
          // { label: 'Вкладка 5', component: shallowRef(CalendarComp) },
        ],
      };
    },
    methods: {
      setActiveTab(index) {
        this.activeTab = index;
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width:100%;
    height:100vh;
  }
  
  .button-row {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  button {
    padding: 10px 20px;
    border: none;
    background-color: #ddd;
    cursor: pointer;
    font-family: Golos-Text-Semibold;
    border-radius: 20px;
  }
  
  button.active {
    background-color: rgb(49,68,104);
    color: white;
    font-family: Golos-Text-Semibold;
  }
  
  .content-block {
    padding: 20px;
    width: 90%;
    height:100%;
  }
  </style>
  