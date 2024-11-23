<template>
    <div class="main-page">
        <NavbarMain/>
        <div class="main-box">
            <div class="card-box">
                <div class="line-main">
                    <div class="logo">
                        <img src="../assets/logo.png">
                    </div>
                    <div class="btn-main" @click="goToMain">
                        На главную
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
                        <b>30</b>
                    </div>
                 </div>
                
                 <div class="line-fifth">
                    <div class="btn-sub" @click="Notification">
                        <div class="text-btn" >Создать уведомление</div>
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
        }
    },
    components : {
        NavbarMain,
        MainPage
    },
    methods: {
        Notification(){
            const response = await axios.post('/api/Notification',{
                event_id : this.$route.query.id,
                count_day : 3
            })
        },  
        goToMain() {
            this.$router.push('/info')
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
    height:100%;
    color:#a3a3a3;
    
    
    text-align: justify;
}

.line-disp {
    display: flex;
    width:80%;
    height:100%;
    flex-direction: row;
    gap:.5vw;
    word-break:break-all;
    padding-left:2vw;
    padding-right:2vw;
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
</style>
