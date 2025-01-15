<template>
    <div class="text-page">
        <div class="text">Подборка новостей</div>
    </div>
    <div class="slider-container">
      <div class="slider">
        <div class="slider-wrapper" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
          <div v-for="(item, index) in newsData" :key="index" class="slider-card">
            <img :src="item['link-img']" alt="news-image" class="slider-card-img" />
            <div class="slider-card-content">
              <p class="slider-card-date">{{ item.date }}</p>
              <p class="slider-card-description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
  
      <button @click="prev" class="slider-btn prev-btn">←</button>
      <button @click="next" class="slider-btn next-btn">→</button>
    </div>

    <div class="text-page">
        <div class="text">Подборка анонсов</div>
    </div>
    <div class="slider-container">
      <div class="slider">
        <div class="slider-wrapper" :style="{ transform: `translateX(-${currentInde * 100}%)` }">
          <div v-for="(item, index) in anonceData" :key="index" class="slider-card">
            <img :src="item['link-img']" alt="anonce-image" class="slider-card-img" />
            <div class="slider-card-content">
              <p class="slider-card-date">{{ item.date }}</p>
              <p class="slider-card-description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
  
      <button @click="preva" class="slider-btn prev-btn">←</button>
      <button @click="nexta" class="slider-btn next-btn">→</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newsData: [],
        anonceData: [],
        currentIndex: 0,
        currentInde: 0,
      };
    },
    mounted() {
      this.fetchNews();
      this.fetchAnonce();
    },
    methods: {
      // Используем fetch для загрузки данных
      async fetchNews() {
        const response = (await fetch('/news.json')).json();
        this.newsData = await response;
        
      },
      async fetchAnonce() {
        const responses = (await fetch('/anonce.json')).json();
        this.anonceData = await responses;
        
      },
      next() {
        if (this.currentIndex < 2) {
          this.currentIndex++;
        } else {
          this.currentIndex = 0;
        }
      },
      prev() {
        if (this.currentIndex > 1) {
          this.currentIndex--;
        } else {
          this.currentIndex = this.newsData.length - 1;
        }
      },

      nexta() {
        if (this.currentInde < 1) {
          this.currentInde++;
        } else {
          this.currentInde = 0;
        }
      },
      preva() {
        if (this.currentInde > 1) {
          this.currentInde--;
        } else {
          this.currentInde = this.newsData.length - 1;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .slider-container {
    position: relative;
    width: 100%;
    overflow: hidden;
    height:40vh;
  }

  .slider-card img {
    width:90%;
    height:60%;
  }
  
  .slider {
    display: flex;
    transition: transform 0.5s ease-in-out;
  }
  
  .slider-wrapper {
    display: flex;
    flex-wrap: nowrap;
  }
  
  .slider-card {
    min-width: 20%;
    box-sizing: border-box;
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #f4f4f4;
    border-radius: 8px;
    margin: 0 10px;
    height:40vh;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  
  .slider-card-content {
    width:90%;
  }
  
  .slider-card-date {
    font-size: 14px;
    color: #888;
    font-family:Golos-Text;
  }
  
  .slider-card-description {
    font-size: 16px;
    color: #333;
    text-align: justify;
    font-family:Golos-Text;
  }
  
  .slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    font-size: 24px;
    padding: 10px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
  }
  
  .prev-btn {
    left: 10px;
  }
  
  .next-btn {
    right: 10px;
  }
  
  .slider-btn:hover {
    background-color: rgba(0, 0, 0, 0.7);
  }

  .text-page {
    width:100%;
    height:10vh;
    display:flex;
    justify-content: start;
    align-items: center;
  }
  .text{
    font-family: Golos-Text-Semibold;
    font-size: 4vh;

  }
  </style>