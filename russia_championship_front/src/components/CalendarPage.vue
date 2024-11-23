<template>
  <div class="main-page">
    <NavbarMain />
    <div class="main-box">
      <div class="text-box">
        <div class="text-label">Интерактивный календарь событий</div>
      </div>
      <div class="description-box">
        <div class="description-label">
          Интерактивный календарь позволит вам просмотреть распределение спортивных событий.
        </div>
      </div>
      <div class="calendar-container">
        <div class="controls">
          <select v-model="selectedYear" class="select-control" @change="updateDays">
            <option :value="2024">2024</option>
          </select>
          <select v-model="selectedMonth" class="select-control" @change="updateDays">
            <option v-for="(month, index) in months" :key="index" :value="index">
              {{ month }}
            </option>
          </select>
          <select v-model="selectedCities" class="select-control" @change="getEvents">
            <option v-for="(city, index) in cities" :key="index" :value="city.city_name">
              {{ city.city_name }}
            </option>
          </select>
        </div>
        <div class="calendar-grid">
          <div
            class="day-cell"
            v-for="(day, index) in calendarDays"
            :key="index"
            :class="{ 'empty-cell': !day.day }"
            @click="openModal(day)"
          >
            <div class="date-line" v-if="day.day">
              <div class="date">{{ day.day }} {{ monthsGenitive[selectedMonth].toLowerCase() }}</div>
            </div>
            <div v-if="day.day && day.events > 0">
              <div class="count-line">{{ day.events }}</div>
              <div class="text-line">событий</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно -->
    <div v-if="isModalVisible" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <h2>События {{ selectedModalDay.day }} {{ monthsGenitive[selectedMonth].toLowerCase() }}</h2>
        <div v-if="selectedModalDay.events > 0">
          <ul>
            <li v-for="(event, index) in selectedModalDayData" :key="index">{{ event }}</li>
          </ul>
        </div>
        <div v-else>
          Нет событий в этот день.
        </div>
        <button class="close-button" @click="closeModal">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavbarMain from "../components/NavbarMain.vue";

export default {
  data() {
    return {
      selectedYear: 2024,
      selectedMonth: 0,
      eventsByDate: {},
      months: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
      monthsGenitive: ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"],
      daysInMonth: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
      calendarDays: [],
      cities: [],
      selectedCities: "г. Казань",
      isModalVisible: false,
      selectedModalDay: null,
      selectedModalDayData: [],
    };
  },
  components: {
    NavbarMain,
  },
  async mounted() {
    this.updateDays();
    this.getEvents();
    this.cities = await (await axios.get("/api/events/all_city")).data;
  },
  methods: {
    async getEvents() {
      try {
        const response = (await axios.post(`/api/events/all_events_with_filters`, { city: this.selectedCities })).data;
        this.processEvents(response);
        this.updateDays();
      } catch (error) {
        console.log(error);
      }
    },
    processEvents(events) {
      this.eventsByDate = {};
      events.forEach((event) => {
        const startDate = new Date(event.Events.date_start);
        const endDate = new Date(event.Events.date_end);
        for (let date = new Date(startDate); date <= endDate; date.setDate(date.getDate() + 1)) {
          const formattedDate = date.toISOString().split("T")[0];
          if (!this.eventsByDate[formattedDate]) {
            this.eventsByDate[formattedDate] = [];
          }
          this.eventsByDate[formattedDate].push(event);
        }
      });
    },
    updateDays() {
      const days = this.daysInMonth[this.selectedMonth];
      const firstDay = new Date(this.selectedYear, this.selectedMonth, 1).getDay();
      const totalCells = 35;
      const daysArray = Array.from({ length: totalCells }, (_, i) => {
        const day = i - firstDay + 1;
        if (day > 0 && day <= days) {
          const formattedDate = `${this.selectedYear}-${String(this.selectedMonth + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
          return { day, events: this.eventsByDate[formattedDate]?.length || 0, data: this.eventsByDate[formattedDate] || [] };
        }
        return { day: null, events: 0, data: [] };
      });
      this.calendarDays = daysArray;
    },
    openModal(day) {
      if (!day.day) return;
      this.selectedModalDay = day;
      this.selectedModalDayData = day.data || [];
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>
  
  <style scoped>
  .main-page {
    width: 100%;
    height: 95vh;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    gap: 2vh;
  }
  
  .main-box {
    width: 100%;
    height: 85vh;
    margin-top: 2vh;
    border-radius: 12px;
  }
  
  .calendar-container {
    max-width: 800px;
    margin: auto;
    text-align: center;
    margin-top:3vh;
  }
  
  .controls {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
  }
  
  .select-control {
    padding: 10px;
    font-size: 16px;
    border:0;
    border-radius: 8px;
    background-color: #ffffff;
    color: #2d3436;
    outline: none;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .select-control:hover {
    border-color: #74b9ff;
  }
  
  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
  }
  
  .day-cell {
    width: 100%;
    aspect-ratio: 1;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    color: #2d3436;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
    font-family:Golos-Text;
  }
  
  .day-cell:hover {
    color: rgb(29, 29, 29);
    transform: scale(1.05);
    cursor:pointer;
  }
  
  .empty-cell {
    background: #ffffff;
    box-shadow: none;
  }

  .empty-cell .count-line {
    display: none;
  }

  .empty-cell .text-line {
    display: none;
  }

  .empty-cell .date-line {
    display:none;
  }

  .date-line {
    color:#fcfcfc;
    font-size:1.1vh;
    height:30%;
    width:100%;
    text-align: end;
    background-color: #dc3d3d;
    display:flex;
    justify-content: end;
    align-items: center;
  }

  .count-line {
    font-family: Golos-Text-Semibold;
    font-size:3vh;
    width:100%;
    height:40%;
    display:flex;
    justify-content: center;
    align-items: center;
  }
  .text-line {
    font-size:1.4vh;
    width:100%;
    height:30%;
    font-family:Golos-Text;
  }

  .date {
    margin-right:.5vw
  }

  .text-box {
    width:100%;
    height:4vh;
    display:flex;
    align-items: center;
  }

  .text-label{
    margin-left:6vw;
    font-size: 4vh;
    color:#000;
    font-family:Golos-Text-Semibold;
  }

  .description-box {
    width:100%;
    height:4vh;
    display:flex;
    align-items: center;
  }

  .description-label{
    margin-left:6vw;
    font-size: 2vh;
    color:#000;
    font-family:Golos-Text;
  }
  .modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  text-align: center;
}

.close-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #ff7675;
  border: none;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.close-button:hover {
  background-color: #d63031;
}
  </style>