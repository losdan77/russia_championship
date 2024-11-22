<template>
    <div class="box">
      <div class="filter-box">
        <div class="line-one">
          <div class="slider-container">
            <div
              class="slider-track"
              @click="toggleSlider"
            >
              <div
                class="slider-thumb"
                :class="{ 'slider-thumb-left': position === 'Россия', 'slider-thumb-right': position === 'Другие страны' }"
              ></div>
            </div>
            <div class="text-slider">{{ position }}</div>
          </div>
        </div>
        <div class="line-two">
          <!-- Субъект -->
          <div class="select-container">
            <label for="subject">Выбор субъекта:</label>
            <v-select
              id="subject"
              class="select-filter"
              v-model="selectedSubject"
              :options="subjects"
              label="name"
              filterable
              placeholder="Начните вводить..."
            />
          </div>
  
          <!-- Город -->
          <div class="select-container">
            <label for="city">Выбор города:</label>
            <v-select
              id="city"
              class="select-filter"
              v-model="selectedCities"
              :options="cities"
              label="name"
              filterable
              multiple
              placeholder="Начните вводить..."
            />
          </div>
  
          <!-- Дата от/до -->
          <div class="date-container">
            <label>Выбор даты:</label>
            <div class="date-inputs">
                <input
                type="date"
                v-model="startDate"
                @change="updateDateRange"
                />
                <input
                type="date"
                v-model="endDate"
                @change="updateDateRange"
                />
            </div>
          </div>
  
          <!-- Вид соревнований -->
          <div class="select-container">
            <label for="competitionType">Вид соревнований:</label>
            <v-select
              id="competitionType"
              class="select-filter"
              v-model="selectedCompetitionType"
              :options="competitionTypes"
              placeholder="Выберите вид"
            />
          </div>
  
          <!-- Тип соревнований -->
          <div class="select-container">
            <label for="eventType">Тип соревнований:</label>
            <v-select
              id="eventType"
              class="select-filter"
              v-model="selectedEventType"
              :options="eventTypes"
              placeholder="Выберите тип"
            />
          </div>
  
          <!-- Половозрастной состав -->
          <div class="select-container">
            <label for="ageGroup">Половозрастной состав:</label>
            <v-select
              id="ageGroup"
              class="select-filter"
              v-model="selectedAgeGroup"
              :options="ageGroups"
              placeholder="Выберите категорию"
            />
          </div>
        </div>
      </div>
      <div class="calendar-box">
        223
      </div>
    </div>
  </template>
  
  <script>
  import "vue-select/dist/vue-select.css";
  import vSelect from "vue-select";
  
  export default {
    components: { vSelect },
    data() {
      return {
        position: "Россия",
        selectedSubject: null,
        selectedCities: [],
        startDate: null,
        endDate: null,
        selectedCompetitionType: null,
        selectedEventType: null,
        selectedAgeGroup: null,
        subjects: [{ name: "Краснодарский край" }, { name: "Москва" }, { name: "Санкт-Петербург" }],
        cities: [{ name: "Краснодар" }, { name: "Сочи" }, { name: "Москва" }, { name: "Санкт-Петербург" }],
        competitionTypes: ["Баскетбол", "Футбол", "Волейбол"],
        eventTypes: ["Чемпионат", "Первенство", "Кубок"],
        ageGroups: ["Женщины 18-25 лет", "Мужчины 18-25 лет", "Юноши до 18 лет", "Девушки до 18 лет"],
      };
    },
    methods: {
      toggleSlider() {
        this.position = this.position === "Россия" ? "Другие страны" : "Россия";
      },
      updateDateRange() {
        console.log("Дата от:", this.startDate, "Дата до:", this.endDate);
      },
    },
  };
  </script>
  
  
  <style scoped>
  .box {
    background-color: rgb(188, 185, 185);
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .filter-box {
    background-color: rgb(255, 255, 255);
    height: 20%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1%;
  }
  
  .calendar-box {
    background-color: rgb(83, 83, 151);
    height: 80%;
    width: 100%;
  }
  
  .line-one {
    background-color: rgb(253, 253, 253);
    width: 100%;
    height: 20%;
    display: flex;
    justify-content: start;
    align-items: center;
  }
  
  .line-two {
    background-color: rgb(252, 252, 252);
    width: 100%;
    height: 70%;
    display:flex;
    gap:1vw;
    flex-direction: row;
  }
  
  
  
  .slider-track {
    width: calc(2.5 * 20px); /* 2.5 раза длиннее квадрата */
    height: 20px;
    background: rgb(249, 249, 249);
    border-radius: 20px; /* Закругленные края */
    position: relative;
    cursor: pointer;
    display: flex;
    align-items: center;
    border:1px solid #ededed;
  }
  
  .slider-thumb {
    width: 20px;
    height: 20px;
    background: rgb(49,68,104);
    border-radius: 10px; /* Немного закругленные края */
    position: absolute;
    top: 0;
    transition: transform 0.3s ease;
  }
  
  .slider-thumb-left {
    transform: translateX(0);
  }
  
  .slider-thumb-right {
    transform: translateX(calc(100% + 10px)); /* Перемещение к правому краю */
  }
  
  .slider-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
  }
  
  .label-left,
  .label-right {
    font-size: 14px;
    color: black;
    font-weight: bold;
  }

  .text-slider {
    font-family: Golos-Text-Semibold;
    font-size:1.4vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color:#a1a1a1;
  }
  .select-container {
    display: flex;
    flex-direction: column;
    align-items: start;
    width:17%;
    justify-content: center;
    align-items: center;
  }
  
  .date-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    align-items: start;
  }

  .date-container input {
    height:3vh;
  }

  .date-container label {
  }
  
  .slider-container {
    width: 80%;
    position: relative;
    display:flex;
    flex-direction: row;
    gap:.5vw;
  }

  .date-inputs {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: start;
  }
  .select-container .select-filter {
    width:100%;
    font-family: Golos-Text;
    cursor: pointer;
  }

  label {
    font-family: Golos-Text;
    font-size:1.5vh;
    display:flex;
    justify-content: start;
    align-items: center;
    width:100%;
  }
  </style>
  