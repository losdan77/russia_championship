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
                    <div class="form-label">Всероссийский чемпионат по плаванию в Башкирии</div>
                    <div class="city-label">
                        <div class="pin-city">г. Верхние подзалупки</div>
                    </div>
                </div>
                <div class="line-two">
                    <div class="vid-label">
                        Плавание 3232321453264265cbvgbxc
                    </div>
                </div>

                <div class="line-three">
                    <div class="disp-label">
                        ОАПОАПЬВАВЫЛОАРВЛОДВЫАЛОДВРЫАЛОВЫАВЫАЛВРЫАЛОрОАПОАПЬВАВЫЛОАРВЛОДВЫАЛОДВРЫАЛОВЫАВЫАЛВРЫАЛОрОАПОАПЬВАВЫЛОАРВЛОДВЫАЛОДВРЫАЛОВЫАВЫАЛВРЫАЛОрОАПОАПЬВАВЫЛОАРВЛОДВЫАЛОДВРЫАЛОВЫАВЫАЛВРЫАЛОр
                    </div>
                    <div class="date-label">
                        11.10.2024 - 13.10.2024
                    </div>
                </div>

                <div class="line-four">
                    <div class="sex-labels">
                    <!-- Блок sex-label завернуть в for -->
                        <div class="sex-label">
                            Мальчики до 25 лет
                        </div>
                    </div>
                    <div class="count-label">
                        Кол-во участников    
                        <b>30</b>
                    </div>
                 </div>
                 <div class="line-fifth">
                    <div class="btn-sub" @click="goToAuth">
                        <img src="../assets/telegram.png">
                        <div class="text-btn">Создать уведомление</div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import NavbarMain from '../components/NavbarMain.vue'
import MainPage from '../components/MainPage.vue'
export default {
    data () {
        return {

        }
    },
    components : {
        NavbarMain,
        MainPage
    },
    methods: {
        goToMain() {
            this.$router.push('/')
        },
        goToAuth() {
            this.$router.push('/auth')
        }
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
    width:80%;
    height:100%;
    padding-left:2vw;
    color:#a3a3a3;
    word-break:break-all;
    padding-right:2vw;
    text-align: justify;
}

.date-label {
    width:20%;
    height:100%;
    display: flex;
    justify-content: center;
    align-items: start;
    color:#a8a8a8;
    font-family:Golos-Text;
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
    width:100%;
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
}

.sex-label {
    padding: 0 2vw;
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
    background-color: #00b8ef;
    font-family: Golos-Text;
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
