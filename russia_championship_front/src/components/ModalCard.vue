<template>
    <div class="main-page">
        <NavbarMain/>
        <div class="main-box">
            <div class="card-box">
                <div class="line-main">
                    <div class="logo">
                        <img src="../assets/logo.png">
                    </div>
                    <div class="line-btns">
                    <div class="btn-main" @click="goToCal">
                        Назад
                    </div>
                    <div class="btn-main" @click="goToMain">
                        На главную
                    </div>
                </div>
                </div>
                <div class="line-one">
                    <div class="form-label">{{ selectedCompetitionType }}</div>
                    <div class="city-label">
                        <div class="pin-city">{{ selectedSubject }}</div>
                </div>
                </div>
                <div class="line-two">
                    <div class="vid-label" >
                        {{ selectedEventType }}
                    </div>
                </div>

                <div class="line-three">
                    <div class="line-disp">
                    <div class="disp-label" v-for="(discip,index) in selectedPrograms"
                    :key="index"
                    >
                        {{ discip.discipline_name }}
                    </div>
                </div>
                    <div class="date-label">
                        {{ startDate }} - {{ endDate }}
                    </div>
                </div>
                
                <div class="line-four">
                    <div class="sex-labels">
                    <!-- Блок sex-label завернуть в for -->
                        <div class="sex-label" v-for="(sex,index) in selectedAgeGroup"
                    :key="index"
                    >
                            {{ sex.sex }}
                        </div>
                    </div>
                    <div class="count-label">
                        Кол-во участников    
                        <b>{{selectedCountGroup}}</b>
                    </div>
                 </div>
                
                 <div class="line-fifth">
                    <div class="btn-sub" @click="showModal = true">
                        <div class="text-btn" >Создать уведомление</div>
                    </div>
                    
                </div>
            </div>
            <!-- Модальное окно -->
            <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
                <div class="modal">
                    <div class="modal-header">Создание уведомления</div>
                    <div class="modal-body">
                        <label for="notificationDays">Укажите за сколько нужно отправить уведомление:</label>
                        <input id="notificationDays" type="number" v-model="notificationDays" class="modal-input"/>
                    </div>
                    <div class="modal-footer">
                        <button class="btn-cancel" @click="showModal = false">Отмена</button>
                        <button class="btn-confirm" @click="createNotification">Создать</button>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'
import MainPage from '../components/MainPage.vue'
import axios from 'axios';
import eventBus from '../eventBus';
export default {
    data () {
        return {
            selectedCompetitionType: null,
            selectedEventType: null,
            selectedAgeGroup: null,
            selectedPrograms:null,
            selectedCountGroup: null,
            selectedSubject: null,
            selectedCities: [],
            startDate: '2024-01-03',
            endDate: '2024-12-11',
            showModal: false,
            notificationDays : 3
        }
    },
    components : {
        NavbarMain,
        MainPage
    },
    methods: {
        async createNotification(){
            try {
                const id = this.$route.query.id
                const count_day = this.notificationDays
                console.log(id,count_day);
                
                const response = await axios.post('/api/events/subscribe_notification',{
                    event_id : id,
                    count_day 
                })
                this.showModal=false
            } catch (error) {
                if (error.status === 409) {
                    console.log(error);
                    eventBus.emit('show-modal', 'Нельзя подписаться на событие, которое закончилось. Попробуйте изменить фильтры для поиска актуальных событий');
                    this.showModal=false
                    return 0
                }
                if (error.status === 405) {
                    console.log(error);
                    eventBus.emit('show-modal', 'Вы уже подписаны');
                    this.showModal=false
                    return 0
                }
                eventBus.emit('show-modal', 'Ошибка при подписке на уведомление, попробуйте позже'); 
                
            }
            
            
        },  
        goToMain() {
            this.$router.push('/info')
        },
        goToCal() {
            this.$router.push('/info/calendar')
        }
    },
    async mounted(){
        const id = this.$route.query.id
        console.log(id);
        const response = await (await axios.get(`/api/events/event_by_id?event_id=${id}`)).data
        console.log(response);
        this.selectedCompetitionType = response.Events.type_championship.type_name
        this.selectedEventType = response.Events.type_sport.type_name
        this.startDate = response.Events.date_start
        this.endDate = response.Events.date_end
        this.selectedSubject = response.Events.city.city_name
        this.selectedAgeGroup = response.Events.sex
        this.selectedPrograms = response.Events.discipline
        this.selectedCountGroup = response.Events.count
        
    }
}
</script>

<style scoped>

.main-page {
    width:100%;
    height:95vh;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    gap:2vh;
}

.main-box {
    width:100%;
    height:85vh;
    margin-top:2vh;
    display: flex;
    justify-content: center;
    align-items:center ;
}

.card-box {
    background-color: rgb(255, 255, 255);
    width:60%;
    height:55%;
    -webkit-box-shadow: 0px 0px 45px -10px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 0px 0px 45px -10px rgba(34, 60, 80, 0.2);
    box-shadow: 0px 0px 45px -10px rgba(34, 60, 80, 0.2);
}
.line-main {
    width:100%;
    height:12%;
    display:flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(49,68,104);
}

.btn-main {
    height:3vh;
    padding: 0 2vw;
    background-color: rgb(255, 255, 255);
    border-radius: .5vh;
    display:flex;
    justify-content: center;
    align-items: center;
    margin-right:1vw;
    color:#1e1e1e;
    font-family:Golos-Text-Semibold;
    font-size: 1.4vh;
}

.btn-main:hover {
    background-color: #c5c5c5;
    color:#161616;
    cursor:pointer;
    transition: all .4s ease;
}
.line-one {
    width:100%;
    height:15%;
    display:flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-top:1%;
}
.form-label {
    width:80%;
    padding-left:2vw;
    font-size:2.5vh;
    font-family:Golos-Text-Semibold;
    line-height: 3vh;
    display:flex;
    justify-content: start;
    align-items: center;
    white-space: nowrap;
}

.city-label {
    width:20%;
    height:100%;
    display:flex;
    justify-content: center;
    align-items: center; 
}

.pin-city {
    width:80%;
    background-color: rgb(49,68,104);
    height:50%;
    overflow:hidden;
    white-space: nowrap;
    display:flex;
    justify-content: center;
    align-items: center;
    color:#fff;
    font-family: Golos-Text;
    font-size:1.3vh;
}

.line-two {
    width:100%;
    height:15%;
}

.vid-label {
    padding-left:2vw;
    font-family:Golos-Text;
    font-size:1.8vh;
    color:#808080;
}


.line-three {
    display:flex;
    flex-direction: row;
    width:100%;
    height:30%;
}

.disp-label {
    flex-wrap: wrap;
    color:#a3a3a3;
    padding: 0;
    display: flex;
    margin-right: .6vw;
    text-align: center;
}

.line-disp {
    display: flex;
    width:80%;
    height:50%;
    flex-direction: row;
    gap:.2vw;
    word-break:break-all;
    padding-left:2vw;
    padding-right:2vw;
    flex-wrap: wrap;
}

.date-label {
    width:20%;
    height:100%;
    display: flex;
    justify-content: center;
    align-items: start;
    color:#a8a8a8;
    font-family:Golos-Text;
    font-size:1.4vh;
}

.logo {
    width:20%;
    height:100%;
    display:flex;
    justify-content: start;
    align-items: center;
}

.logo img {
    width:40px;
    height:40px;
    margin-left:2vw;
}

.line-four {
    
    height:13%;
    display: flex;
    flex-direction: row;
}

.sex-labels {
    width: 80%;
    height:100%;
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center ;
    gap:.5vw;
    margin-left:2vw;
}

.sex-label {
    font-size: 1.5vh;
    font-family: Golos-Text;
}

.count-label {
    width:20%;
    height:100%;
    display:flex;
    flex-direction:column;
    align-items: center;
    justify-content: center;
    font-size: 1.5vh;
    color:#616161;
    text-align: center;
    font-family: Golos-Text;
}

.line-fifth {
    width:100%;
    height:10%;
    display: flex;
    flex-direction: row;
    justify-content: end;
    align-items: center;
}

.btn-sub {
    background-color: #ff9b05;
    font-family: Golos-Text-Semibold;
    font-size:1.4vh;
    width:25%;
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height:3.5vh;
    border-radius: 1vw;
    margin-right:2.5%;
    color:#fff;
    gap:.5vw;
}

.btn-sub img {
    width:25px;
    height:25px;
}

.btn-sub:hover {
    background-color: #a8a8a8;
    transition: all .4s ease;
    cursor:pointer;
}
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal {
    background: white;
    padding: 20px;
    border-radius: 10px;
    width: 500px;
    height:200px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: Golos-Text;
}

.modal-header {
    font-size: 18px;
    margin-bottom: 15px;
    font-family:Golos-Text;
}

.modal-body {
    margin-bottom: 15px;
}

.modal-input {
    width: 30%;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.modal-footer {
    display: flex;
    justify-content: space-between;
    height:15%;
    width:65%;
    gap:.5vw;
}

.btn-cancel {
    background: #4a4a4a;
    color: white;
    border: none;
    display:flex;
    justify-content:center;
    align-items:center;
    border-radius: 5px;
    cursor: pointer;
    font-family:Golos-Text-Semibold;
    font-size:1.5vh;
    padding: 0 2vw;
    margin-left: 1vw;
}

.btn-cancel:hover {
    background: #a5a5a5;
    transition: all .4s ease;
}

.btn-confirm {
    background: #ff820d;
    color: white;
    border: none;
    display:flex;
    justify-content:center;
    align-items:center;
    border-radius: 5px;
    cursor: pointer;
font-family:Golos-Text-Semibold;
    font-size:1.5vh;
    padding: 0 2vw;
    margin-right: 1vw;
}

.btn-confirm:hover {
    background: #f1f1f1;
color:#000;
transition: all .4s ease;
}

.line-btns {
    display:flex;
    flex-direction: row;
    justify-content: end;
    align-items: center;
    width:40vw;
    gap:.1vw;
}
</style>