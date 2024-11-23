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
            @update:modelValue="filter"
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
            @update:modelValue="filter"
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
              @change="filter"

              />
              <input
              type="date"
              class="date-input"
              v-model="endDate"

              @change="filter"
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
            @update:modelValue="filter"
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
            @update:modelValue="filter"
            
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
            :selectedAgeGroup
            @update:modelValue="filter"
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
            @update:modelValue="filter"
            label ='discipline_name'
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
            @update:modelValue="filter"
            label ='count'
            
          />
        </div>
      </div>
      <div class="box-checkbtn">
    <label>
      <input 
        type="checkbox" 
        v-model="mainCheckbox1"
        :disabled="isAnyChecked && !mainCheckbox1"
      />
      1 мес.
    </label>
    <label>
      <input 
        type="checkbox" 
        v-model="mainCheckbox2" 
        :disabled="isAnyChecked && !mainCheckbox2"
        />
        
      3 мес.
    </label>
    <label>
      <input 
        type="checkbox" 
        v-model="mainCheckbox3" 
        :disabled="isAnyChecked && !mainCheckbox3"
        />
      6 мес.
    </label>
    <button @click="toggleMoreFilters" class="btn-checkbox">
      {{ showMoreFilters ? "Скрыть" : "Еще" }}
    </button>
    <transition name="slide-up" class="transition">
    <div v-if="showMoreFilters" class="additional-filters">
      <label>
        <input 
        type="checkbox" 
        v-model="extraCheckbox1"
        :disabled="isAnyChecked && !extraCheckbox1" 
        />
        Ближайшие мероприятия
      </label>
      <label>
        <input 
          type="checkbox" 
          v-model="extraCheckbox2" 
          :disabled="isAnyChecked && !extraCheckbox2"
          />
        Мероприятия текущей недели
      </label>
      <label>
        <input 
          type="checkbox" 
          v-model="extraCheckbox3" 
          :disabled="isAnyChecked && !extraCheckbox3"
          />
        Мероприятия следующего месяца
      </label>
      <label>
        <input 
          type="checkbox" 
          v-model="extraCheckbox4" 
          :disabled="isAnyChecked && !extraCheckbox4"/>
        Мероприятия полугодия
      </label>
    </div>
  </transition>
  </div>

  <!-- Выплывающий блок с дополнительными чекбоксами -->
  

      <div class="btns-filter">
        <div class="btns-filter-save-delete">
        <div class="btn-save-filter" @click="saveFilter">
          Запомнить фильтр
        </div>
        <div class="btn-delete-filter" @click="deleteFilter">
          X
        </div>
        </div>
        <div class="btn-save-filter" id="btn-calendar" @click="saveFilter">
          Календарь
        </div>
      </div>
      </div>
    </div>
    <div class="calendar-box" v-if="events.length "  :class="{ 'dimmed': loading }">
      <div 
        class="card-event" 
        v-for="(event, index) in events" 
        :key="index"
      >
        <!-- Линия 1 -->
        <div class="card-line-1">
          <div class="type-event">{{ event.Events.type_championship.type_name }}</div>
          <div class="date-event">
            {{ new Date(event.Events.date_start).toLocaleDateString() }} - 
            {{ new Date(event.Events.date_end).toLocaleDateString() }}
          </div>
        </div>

        <!-- Линия 2 -->
        <div class="card-line-2">
          <div class="description-events">
          <div class="description-event" 
          v-for="(discipline,index) in event.Events.discipline"
          :key="index"
          >
            {{ discipline.discipline_name || 'Описание отсутствует' }}
          </div>
        </div>
          <div class="date-event">
            
          </div>
        </div>

        <!-- Линия 3 -->
        <div class="card-line-3">
          <div class="pins">
            <div class="pin">{{ event.Events.type_sport.type_name }}</div>
            <div class="pins-second">
              <div class="pin-2" v-for="(group, idx) in event.Events.sex" :key="idx" v-if="event.Events.sex.length">
                  {{ group.sex }}
              </div>
              <div class="pin-2" v-else>
                Категории не указаны
              </div>
            </div>
          </div>
          <div class="date-event">{{ event.Events.city.city_name }}</div>
        </div>
      </div>
    </div>
    <div v-if="loading" class="loading-spinner"></div>
    <div class="calendar-box" v-if="!events.length && !loading" >Ничего нет</div>
    </div>
  </template>

  <script>
  import "vue-select/dist/vue-select.css";
  import vSelect from "vue-select";
  import eventBus from '../eventBus';
  import axios from "axios";
  export default {
    components: { vSelect },
    data() {
      return {
        loading: false,
        position: "Россия",
        selectedSubject: null,
        selectedCities: [],
        startDate: '2024-01-03',
        endDate: '2024-12-11',
        selectedCompetitionType: null,
        selectedEventType: null,
        selectedAgeGroup: null,
        selectedPrograms:null,
        selectedCountGroup: null,
        subjects: [],
        cities: [],
        competitionTypes: [],
        eventTypes: [],
        ageGroups: [],
        countGroup : [],
        programTypes : [],
        events : [],
        mainCheckbox1: false,
        mainCheckbox2: false,
        mainCheckbox3: false,
        // Дополнительные чекбоксы
        extraCheckbox1: false,
        extraCheckbox2: false,
        extraCheckbox3: false,
        extraCheckbox4: false,
        // Видимость дополнительного блока
        showMoreFilters: false,
      };
    },
    
    
    methods: {
      async filter(){
        this.loading = true
        console.log(this.selectedPrograms); 
        try {
          console.log(this.selectedSubject?this.selectedSubject.subject_name : null);
          console.log(this.selectedCities[0]? this.selectedCities[0].city_name : null);
          console.log(this.selectedPrograms? this.selectedPrograms.discipline_name:null );
          console.log(this.selectedCountGroup?this.selectedCountGroup.count : null);
          console.log(this.selectedAgeGroup? this.selectedAgeGroup.sex:null);
          console.log(this.startDate);
          console.log(this.endDate);
          console.log(this.selectedEventType ? this.selectedEventType.type_name : null);
          console.log(this.selectedCompetitionType ? this.selectedCompetitionType.type_name : null);
          

          

          const response = (await axios.post(`/api/events/all_events_with_filters`,{
            subject : this.selectedSubject?this.selectedSubject.subject_name : null,
            city : this.selectedCities[0]? this.selectedCities[0].city_name : null,
            type_sport_name: this.selectedCompetitionType ? this.selectedCompetitionType.type_name: null ,
             type_championship_name : this.selectedEventType ? this.selectedEventType.type_name : null,
            sex_name : this.selectedAgeGroup? this.selectedAgeGroup.sex:null,
            discipline_name : this.selectedPrograms? this.selectedPrograms.discipline_name:null,
            count_values : this.selectedCountGroup?this.selectedCountGroup.count : null,
            date_start : this.startDate,
            date_end : this.endDate
          })).data
          this.loading=false 
          this.events = response
          console.log(this.events);
          if (response.length ===0) {
            eventBus.emit('show-modal', 'По вашему запросу ничего не найдено, вы можете увеличить временные промежутки или изменить'); 
            return 0
          }

        } catch (error) {
          console.log(error.status);
          if (error.status===409) {
            eventBus.emit('show-modal', 'Дата начала не может быть больше даты окончания');  
            return 0
          }
          if (error) {
            eventBus.emit('show-modal', 'Непридвиденная ошибка');  
            this.loading=false 
            return 0
          }

        }

        // }
      },  
      async citiesBySub(){
        try {
          this.cities = (await axios.get(`/api/events/all_city_in_subject?id_subject=${this.selectedSubject.id}`)).data
        } catch (error) {
          // eventBus.emit('show-modal', 'Для более точного поиска рекомендуется выбрать субъект');  
        }
      },

      toggleSlider() {
        this.position = this.position === "Россия" ? "Другие страны" : "Россия";
      },
      updateDateRange() {
        console.log("Дата от:", this.startDate, "Дата до:", this.endDate);
      },
      async deleteFilter(){
        localStorage.removeItem('filters')
        selectedSubject = null
        selectedCities = []
        startDate ='2024-01-03',
        endDate = '2024-12-11',
        selectedCompetitionType = null
        selectedEventType = null
        selectedAgeGroup = null
        selectedPrograms = null
        selectedCountGroup = null

        await this.filter()
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
        Bus
      },
      toggleMoreFilters() {
      this.showMoreFilters = !this.showMoreFilters;
    },
      
    },
      computed: {
      // Определяет, выбран ли хотя бы один чекбокс
      isAnyChecked() {
        return (
          this.mainCheckbox1 ||
          this.mainCheckbox2 ||
          this.mainCheckbox3 ||
          this.extraCheckbox1 ||
          this.extraCheckbox2 ||
          this.extraCheckbox3 ||
          this.extraCheckbox4
        );
      },
    },
    async mounted(){
      try {
        this.loading = true
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

        this.subjects =  await (await axios.get('/api/events/all_subjects')).data
        this.cities = (await axios.get('/api/events/all_city')).data
        this.ageGroups = (await axios.get('/api/events/all_city')).data
        this.eventTypes = (await axios.get('/api/events/all_type_championship')).data
        this.competitionTypes = (await axios.get('/api/events/all_type_sport')).data
        this.ageGroups = (await axios.get('/api/events/all_sex')).data
        this.events = (await axios.post('/api/events/all_events_with_filters',{})).data
        this.programTypes = (await axios.get('/api//events/all_discipline')).data
        this.countGroup = (await axios.get('/api/events/all_count_values')).data
        // this.selectedPrograms = (await axios.post('/api/events/all_events_with_filters')).data
        console.log(this.events );
        this.loading=false 
      } catch (error) {
        console.log(error);
        this.loading=false 
        eventBus.emit('show-modal', 'Непридвиденная ошибка');  
        
      }
    },
    //типовой запрос, админка, заслуженный тренер россии, юзабилити тестирование
    watch: {
        
    },
  };
  </script>
  
  
<style scoped>

  .box {
    background-color: rgb(255, 255, 255);
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
    width:60%;
    justify-content: center;
    align-items: center;
  }
  .select-container-4 {
    display: flex;
    flex-direction: column;
    align-items: start;
    width:35%;
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
    width:45%;
}
.btns-filter {
  display:flex;
  flex-direction: row;
  justify-content: space-between;
  width:25%;
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
  font-size:1.2vh;
}
.btn-delete-filter {
  background-color: #bd4545;
  color:#fff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family:Golos-Text;
  height:4vh;
  border-radius: 50%;
  width:2vw;
  font-size:1.5vh;
  font-family: Golos-Text-Semibold;
  cursor: pointer;
}
#btn-calendar {
  background-color: rgb(49,68,104);
}

#btn-calendar:hover {
  background-color: rgb(32,44,67);
}

.box-checkbtn {
  width:25%;
  height:100%;
  display:flex;
  flex-direction: row;
  justify-content:space-between;
  align-items:center;
}

.btn-save-filter:hover {
  transition: all .3s ease;
  background-color: #a1a1a1;
  cursor: pointer;
}

/* CALENDAR */
.calendar-box {
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
.description-events {
  line-height: 2vh;
  display: flex;
  justify-content: start;
  align-items: start;
  flex-direction: row;
  height:100%;
  width:80%;
  gap:1vw;
  margin-left:1vw;
  color:#c5c5c5;
  overflow: hidden;
  white-space:nowrap;
  
}

.description-event {
  font-family:Golos-Text;
  font-size: 1.5vh;
  line-height: 2vh;
  display: flex;
  justify-content: start;
  align-items: start;
  height:100%;
  color:#c5c5c5;
  overflow: hidden; 
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


  .additional-filters {
  position: absolute;
  padding: 1vw;
  width:100%;
  background: #f5f5f5;
  border: 1px solid #dfdfdf;
  margin-top:20.5vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: Golos-Text;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;
}

.slide-up-enter {
  transform: translateY(-10px);
  opacity: 0;
}

.slide-up-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}

.transition {
  background-color: #ffffff;
  width:20.5%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btn-checkbox {
  height:4vh;
  border:0;
  width:70%;
  font-family: Golos-Text;
  font-weight: 600;
  border-radius: 2vw;
}

.box-checkbtn label {
  font-family: Golos-Text;
  color:#515151;
}

.btns-filter-save-delete {
  display:flex;
  flex-direction: row;
  gap:.4vw;
}


.calendar-box.dimmed {
  filter: brightness(0.4); /* Применить затемнение */
}

.loading-spinner {
  border: 8px solid #3b3b3b; /* Цвет фона */
  border-top: 8px solid rgb(41,98,255); /* Цвет верхней части */
  border-radius: 50%;
  width: 40px; /* Ширина */
  height: 40px; /* Высота */
  animation: spin 1s linear infinite; /* Анимация */
  margin: 20px auto; /* Центрирование */
  position: absolute;
  margin-left:43vw;
  margin-top:30vh;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
  </style>