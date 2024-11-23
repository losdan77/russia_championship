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
          
          <div class="select-container" >
            <label for="subject">Выбор субъекта:</label>
            <v-select
              id="subject"
              class="select-filter"
              v-model="selectedSubject"
              :options="subjects"
              label="subject_name"
              filterable
              placeholder="Начните вводить"
              @update:modelValue="citiesBySub"
              @input="citiesBySub"
              :selectedSubject
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
              label="city_name"
              filterable
              multiple
              placeholder="Начните вводить"
            />
          </div>
  
          <!-- Дата от/до -->
          <div class="date-container">
            <label>Выбор даты:</label>
            <div class="date-inputs">
                <input
                type="date"
                class="date-input"
                v-model="startDate"
                @change="updateDateRange"
                />
                <input
                type="date"
                class="date-input"
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
              label ='type_name'
              :options="competitionTypes"
              placeholder="Выберите вид"
              :selectedCompetitionType
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
              label ='type_name'
              placeholder="Выберите тип"
              :selectedEventType
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
              label ='sex'
              :selectedEventType
            />
          </div>
        </div>
        <div class="line-three">
          <div class="line-input">
            <!-- Дисциплина / Программа -->
          <div class="select-container-2">
            <label for="eventType">Дисциплина / Программа:</label>
            <v-select
              id="eventType"
              class="select-filter"
              v-model="selectedPrograms"
              :options="programTypes"
              
              placeholder="Выберите дисциплину / программу"
            />
          </div>
          
          
          <!-- Количество участников -->
          <div class="select-container-4">
            <label for="ageGroup">Количество участников:</label>
            <v-select
              id="ageGroup"
              class="select-filter"
              v-model="selectedCountGroup"
              :options="countGroup"
              placeholder="Выберите кол-во"
            />
          </div>
        </div>
        <div class="btn-save-filter" @click="saveFilter">
          Запомнить фильтр
        </div>
        </div>
      </div>
      <div class="calendar-box">
        <div 
          class="card-event" 
          v-for="(event, index) in events" 
          :key="index"
        >
          <!-- Линия 1 -->
          <div class="card-line-1">
            <div class="type-event">{{ event.title }}</div>
            <div class="date-event">{{ event.date }}</div>
          </div>

          <!-- Линия 2 -->
          <div class="card-line-2">
            <div class="description-event">{{ event.description }}</div>
            <div class="date-event">{{ event.location }}</div>
          </div>

          <!-- Линия 3 -->
          <div class="card-line-3">
            <div class="pins">
              <div class="pin">{{ event.sport }}</div>
              <div class="pins-second">
                <div 
                  class="pin-2" 
                  v-for="(group, idx) in event.ageGroups" 
                  :key="idx"
                >
                  {{ group }}
                </div>
              </div>
            </div>
            <div class="date-event">{{ event.city }}</div>
          </div>
        </div>
      </div>
      </div>
    </template>
  
  <script>
  import "vue-select/dist/vue-select.css";
  import vSelect from "vue-select";
  import axios, { all } from "axios";
  import eventBus from '../eventBus';
  export default {
    components: { vSelect },
    data() {
      return {
        position: "Россия",
        filters : {
          selectedSubject: null,
          selectedCities: [],
          startDate: null,
          endDate: null,
          selectedCompetitionType: null,
          selectedEventType: null,
          selectedAgeGroup: null,
          selectedPrograms:null,
          selectedCountGroup: null,
        },
        subjects: [],
        cities: [],
        competitionTypes: [],
        eventTypes: [],
        ageGroups: [],
        countGroup : [],
        programTypes : [],
        all : []
      };
    },
    
    
    methods: {
      async citiesBySub(){
        try {
          this.cities = (await axios.get(`/api/events/all_city_in_subject?id_subject=${this.selectedSubject.id}`)).data
        } catch (error) {
          eventBus.emit('show-modal', 'Для более точного поиска рекомендуется выбрать субъект');  
        }
      },

      toggleSlider() {
        this.position = this.position === "Россия" ? "Другие страны" : "Россия";
      },
      updateDateRange() {
        console.log("Дата от:", this.startDate, "Дата до:", this.endDate);
      },
      saveFilter() {
        console.log(this.selectedCities);

        localStorage.setItem('filters', 
        JSON.stringify({
          selectedSubject: this.selectedSubject,
          selectedCities: this.selectedCities,
          startDate: this.startDate,
          endDate: this.endDate,
          selectedCompetitionType: this.selectedCompetitionType,
          selectedEventType: this.selectedEventType,
          selectedAgeGroup: this.selectedAgeGroup,
          selectedPrograms: this.selectedPrograms,
          selectedCountGroup: this.selectedCountGroup,
        }));
        console.log('good');
      }
      
    },
    computed : {
      
    },
    async mounted(){
      try {
        const savedFilters = localStorage.getItem('filters');
        if (savedFilters) {
          const parsedFilters = JSON.parse(savedFilters);
          
          if (parsedFilters.selectedSubject) this.selectedSubject = parsedFilters.selectedSubject;
          if (parsedFilters.selectedCities) this.selectedCities = parsedFilters.selectedCities;
          if (parsedFilters.startDate) this.startDate = parsedFilters.startDate;
          if (parsedFilters.endDate) this.endDate = parsedFilters.endDate;
          if (parsedFilters.selectedCompetitionType) this.selectedCompetitionType = parsedFilters.selectedCompetitionType;
          if (parsedFilters.selectedEventType) this.selectedEventType = parsedFilters.selectedEventType;
          if (parsedFilters.selectedAgeGroup) this.selectedAgeGroup = parsedFilters.selectedAgeGroup;
          if (parsedFilters.selectedPrograms) this.selectedPrograms = parsedFilters.selectedPrograms;
          if (parsedFilters.selectedCountGroup) this.selectedCountGroup = parsedFilters.selectedCountGroup;
          
        }
        const all_countrys = (await axios.get('/api/events/all_countrys')).data
        this.subjects =  await (await axios.get('/api/events/all_subjects')).data
        this.cities = (await axios.get('/api/events/all_city')).data
        this.ageGroups = (await axios.get('/api/events/all_city')).data
        this.eventTypes = (await axios.get('/api/events/all_type_championship')).data
        this.competitionTypes = (await axios.get('/api/events/all_type_sport')).data
        this.ageGroups = (await axios.get('/api/events/all_sex')).data
        this.all = (await axios.get('/api/events/all_events_with_filters')).data


        
      } catch (error) {
        console.log(error);
        
      }
    },
    
    watch: {
        
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
    width: 100%;
    height: 20%;
    display: flex;
    justify-content: start;
    align-items: center;
  }
  
  .line-two {
    width: 100%;
    height: 35%;
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

  .select-container-2 {
    display: flex;
    flex-direction: column;
    align-items: start;
    width:50%;
    justify-content: center;
    align-items: center;
  }
  .select-container-3 {
    display: flex;
    flex-direction: column;
    align-items: start;
    width:30%;
    justify-content: center;
    align-items: center;
  }
  .select-container-4 {
    display: flex;
    flex-direction: column;
    align-items: start;
    width:20%;
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
    gap:.5vw;
  }
  .select-container .select-filter {
    width:100%;
    font-family: Golos-Text;
    cursor: pointer;
  }

  .select-container-2 .select-filter {
    width:100%;
    font-family: Golos-Text;
    cursor: pointer;
  }

  .select-container-3 .select-filter {
    width:100%;
    font-family: Golos-Text;
    cursor: pointer;
  }
  .select-container-4 .select-filter {
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

  .v-select * {
    border:0;
    background-color: #f9f9f9;
    font-family:Golos-Text;
    font-size:1.5vh;
}

.date-input{
  background-color: #f9f9f9;
  padding:.2vh;
  border:0;
}
/* Шел 10 час перемещения блоков */
.line-three {
  width: 100%;
    height: 35%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.line-input {
  display:flex;
    gap:2%;
    flex-direction: row;
    width:65.5%;
}

.btn-save-filter {
  background-color: #2a2a2a;
  color:#fff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family:Golos-Text;
  height:4vh;
  border-radius: 2vh;
  padding:0 2vw;
}

.btn-save-filter:hover {
  transition: all .3s ease;
  background-color: #a1a1a1;
  cursor: pointer;
}

/* CALENDAR */
.calendar-box {
    background-color: rgb(83, 83, 151);
    height: 80%;
    width: 100%;
    overflow-y: scroll;
    gap:.2vh;
    scrollbar-width: thin; /* Установите тонкую полосу прокрутки */
    scrollbar-color: rgb(83, 83, 151)rgb(222, 222, 222);
  }

.card-event {
  background-color: #ffffff;
  border-top:1px solid #ddd;
  width:100%;
  height:10vh;
  display: flex;
  flex-direction: column;
  padding: 1vh 0;
}

.card-line-1 {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.type-event {
  font-family: Golos-Text-Semibold;
  font-size: 1.9vh;
  line-height: 3vh;
  display: flex;
  justify-content: start;
  align-items: center;
  height:100%;
  margin-left:1vw;
  width:50%;
  overflow:hidden;
  white-space: nowrap; /* Отменяем перенос текста */
  overflow: hidden; /* Обрезаем содержимое */
  text-overflow: ellipsis;
}

.description-event {
  font-family:Golos-Text;
  font-size: 1.5vh;
  line-height: 2vh;
  display: flex;
  justify-content: start;
  align-items: start;
  height:100%;
  margin-left:1vw;
  width:70%;
  color:#c5c5c5;
  white-space: nowrap;
  overflow: hidden;
  white-space: nowrap; /* Отменяем перенос текста */
  overflow: hidden; /* Обрезаем содержимое */
  text-overflow: ellipsis;
}

.date-event {
  line-height: 2vh;
  font-family: Golos-Text;
  font-size: 1.4vh;
  display: flex;
  justify-content: center;
  align-items: center;
  height:100%;
  color:#a1a1a1;
  width:15%;
}

.card-line-2 {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top:.5vh;
}

.card-line-3 {
  display: flex;
  margin-top:1vh;
  flex-direction: row;
  justify-content: space-between;
}
.pins {
  display: flex;
  flex-direction: row;
  gap:.3vw;
  margin-left:1vw;
  width:75%;
  overflow:hidden
}

.pin {
  font-family: Golos-Text;
  font-size:1.4vh;
  color:#555555;
  background-color: rgba(49, 68, 104, 0.155);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 1vw;
  height:2vh;
  padding: 0 1vw;
}

.pins-second {
  font-family: Golos-Text;
  font-size:1.4vh;
  color:#555555;
  background-color: rgba(49, 68, 104, 0.155);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 1vw;
  height:2vh;
  padding:0 1vw;
  gap:.7vw;
}

.pin-2 {
  font-family: Golos-Text;
  font-size:1.4vh;
  color:#555555;
  display: flex;
  justify-content: center;
  align-items: center;
  height:2vh;
  white-space: nowrap; /* Отменяем перенос текста */
  overflow: hidden; /* Обрезаем содержимое */
  text-overflow: ellipsis;
}

label {
    font-family: Golos-Text;
    font-size:1.5vh;
    display:flex;
    justify-content: start;
    align-items: center;
    width:100%;
    color:#9d9d9d;
  }
  </style>
