<template>
  <div class="window">
      <section class="left-section">
        <div class="section" id="section-1">
          <div class="content-section-1">
            <div class="logo-img">
              <img src="../assets/logo.png" @click="goToHome"/>
            </div>
            <div class="text-box">
              Министерство спорта
            </div>
            <div class="text-box-2">
              календарь событий
            </div>
          </div>
        </div>
      </section>
      <section class="right-section">
        <div class="section" id="section-2">
          <div class="upper-wrapper">
            Вход
          </div>
          <div class="input-wrapper">
            <form @submit.prevent="submitForm">
            <div class="wrapper-input">
              <label for="email">Email</label>
              <input type="email" id="email" v-model="email"  required/>
            </div>
            <div class="wrapper-input">
              <label for="password">Пароль</label>
              <input type="password" id="password" v-model="password" required />
            </div>
          </form>
          </div>
          <div class="box-password-recovery">
            <div class="btn-password-recovery" @click="GoToRestoring">Забыли пароль?</div>
          </div>
          <div class="btn-wrapper">
            <div class="btn-reg" @click="GoToReg()">ЕЩЕ НЕ ЗАРЕГИСТРИРОВАНЫ?</div>
            <div class="btn-sign-in" @click="Authorization()">ВОЙТИ</div>
          </div>
          <div class="sign-in-botton-line">
            <div class="text-sign-in-bottom">Вход через:</div> 
            <div class="fast-auth-box">
              <div class="btn-google">
                <div class="icon-btn">
                  <img src="../assets/google.png">
                </div>
                <div class="text-btn"  
                @click="openWindow"
                >
                Войти через Google
                </div>
              </div>
                <div class="btn-yandex">
                <div class="icon-btn">
                  <img src="../assets/yandex.png">
                  </div>
                  <div class="text-btn"  
                  @click="openWindowYandex"
                  >
                  Войти через Яндекс
                  </div>
              </div>
            </div>
            <div class="btn-go-register" @click="GoToReg">
              <div class="icon-btn">
                <img src="../assets/yandex.png">
              </div>
              <div class="text-btn">Еще не зарегистрированы?</div>
            </div>
          </div>
        </div>
      </section>
    </div>

    </template>
<script>
import axios from 'axios';
import { GoogleLogin } from 'vue3-google-login';
import ModalLogin from './Modals/GlobalModal.vue';
import eventBus from '../eventBus';

  export default {
    data() {
      return {
        email: '',
        password: '',
        code : null,
        showModal: false,
        modalMessage: '',
      };
    },
    components : {
      GoogleLogin,
      ModalLogin
    },
    methods: {
      async exchangeCodeForToken() {
        // Отправляем код на сервер
        const response = await axios.get(`/api/user/auth/google?code=${this.code}`)
        console.log(this.code);
        console.log(response.data);
      },
      GoToRestoring(){
        this.$router.push('/user/restoring')
      },
      GoToReg(){
        this.$router.push('/reg')
      },  
      async Authorization(){
        try {
          const response = await axios.post('/api/user/login', {
          email: this.email,
          password: this.password,
        });
        if (response.status === 200) {
          eventBus.emit('show-modal', 'Вы успешно авторизованы');
          return this.$router.push('/profile')
        }
        } catch (error) {
          
          if (error.response.status === 401) {
          eventBus.emit('show-modal', 'Неправильный Email или пароль');
          return 0
        }
        if (error.response.status === 422) {
          eventBus.emit('show-modal', 'Пропущенно одно или несколько обязательных полей');
          return 0
        }
          eventBus.emit('show-modal', 'Непридвиденная ошибка, попробуйте через несколько минут');
        }
      },
      async openWindow() {
        const url = await axios.get('/api/user/login/google')
        console.log(url.data);
        const newWindow = window.open(url.data, '_blank');
        if (newWindow) {
          newWindow.blur();
        }
        window.open('http://localhost:5173/', '_self');
      },


      async openWindowYandex() {
        const url = await axios.get('/api/user/login/yandex')
        console.log(url.data);
        const newWindow = window.open(url.data, '_blank');
        if (newWindow) {
          newWindow.blur();
        }
        window.open('http://localhost:5173/', '_self');
      }
    },
    created() {
    const urlParams = new URLSearchParams(window.location.search);
    this.code = urlParams.get('code'); 

    if (this.code) {
      this.exchangeCodeForToken();
    }
  },
  };
  </script>
  
  <style scoped>
  @font-face {
      font-family: Golos-Text-Semibold;
      src: url('../assets/fonts/Golos_Text/static/GolosText-SemiBold.ttf');
    }
  
  @font-face {
      font-family: Golos-Text;
      src: url('../assets/fonts/Golos_Text/static/GolosText-Regular.ttf');
    }
  
    .window {
    display: flex;
    width: 50%;
    height:50%;
    position:absolute;
    left:0;
    right:0;
    top:0;
    bottom:0;
    margin:auto;
    -webkit-box-shadow: 0px 0px 49px 0px rgba(34, 60, 80, 0.2);
  -moz-box-shadow: 0px 0px 49px 0px rgba(34, 60, 80, 0.2);
  box-shadow: 0px 0px 49px 0px rgba(34, 60, 80, 0.2);
  }
  
  .left-section {
    width: 50%;
    background-color: #f0f0f0;
  }
  
  .right-section {
    width: 50%;
    border: 1px solid #f5f5f5;
    background-color: #ddd;
  }
  
  .section {
    background-color: #ffffff;
    display:flex;
    flex-direction: column;
    width:100%;
    height:100%;
  }
  
  #section-1 {
    background: url('../assets/fon.PNG');
    background-size:cover;
    background-repeat:no-repeat;
    background-color: #aaa;
  }
  
  .content-section-1 {
    position: relative;
    width:100%;
    height:100%;
  }
  
  .logo-img {
    position: absolute;
    top:-1vw;
    bottom:0;
    left:0;
    right:0;
    margin:auto;
    text-align: center;
    align-content: center;
  }
  
  .text-box {
    position: absolute;
    top:3vw;
    bottom:0;
    left:0;
    right:0;
    margin:auto;
    text-align: center;
    align-content: center;
    color:#fff;
    font-family: Golos-Text;
    font-size:1.7vh;
    line-height: 2vh;
  }
  
  .text-box-2 {
    position: absolute;
    top:4.5vw;
    bottom:0;
    left:0;
    right:0;
    margin:auto;
    text-align: center;
    align-content: center;
    color:#fff;
    font-family: Golos-Text;
    font-size:1.5vh;
    line-height: 2vh;
  }
  
  .logo-img img {
    width:3vw;
    height:3vw;
  }
  
  
  .upper-wrapper {
    padding:3vh 0 0 3vh;
    height:4vh;
    font-size:3vh;
    font-family: Golos-Text;
    color:#1d1d1d;
    font-weight: 600;
  }
  
  .input-wrapper {
    display: flex;
    flex-direction: column;
    padding-bottom:2vh;
    padding-top:2vw;
    padding: 2vw 3vh 2vh 3vh;
  }
  
  .input-wrapper label {
    height:2vh;
    padding-left:3vh;
    padding-top:.5vh;
    font-size: 1.5vh;
    color:#919191;
    font-family: Golos-Text;
    background-color: #f0f0f0;
  }
  
  .input-wrapper input {
    background-color: #f0f0f0;
    outline: 0;
    border:0;
    height:3vh;
    padding-left:3.5vh;
    font-size: 1.8vh;
    font-family: Golos-Text;
    cursor:pointer;
  }
  
  .wrapper-input {
    display:flex;
    flex-direction: column;
    margin-top:.5vh;
    border-bottom:1px solid #eeeeee;
  }
  
  .wrapper-input:hover {
    transition: all .4s ease;
    border-bottom:1px solid #9d9d9d;
    cursor:pointer;
  }
  
  .btn-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding:1vh 1.5vw;
  }
  
  .btn-sign-in {
    display: flex;
    background-color: rgb(49,68,104);
    font-size:1.6vh;
    align-items: center;
    justify-content: center;
    height:5vh;
    width:35%;
    font-family: Golos-Text-Semibold;
    color:#fff;
  }
  
  .btn-sign-in:hover {
    background-color: rgb(33,44,67);
    cursor:pointer;
    transition: all .4s ease;
  }
  
  .btn-reg {
    height:4vh;
    text-align: center;
    align-content: center;
    font-family: Golos-Text;
    font-weight: 300;
    font-size:1.4vh;
    color:#a3a3a3;
    height:5vh;
    width:60%;
    border:1px solid #ececec;
  }
  
  .btn-reg:hover {
    background-color: #ffffff;
    color:rgb(49,68,104);
    border:1px solid rgb(49,68,104);
    cursor:pointer;
    transition: all .4s ease;
  }
  
  .box-password-recovery {
    padding: .5vh 1.5vw;
  }
  
  .btn-password-recovery {
    font-size:1.6vh;
    font-family: Golos-Text;
    display: flex;
    justify-content: left;
    align-items: center;
    color:#8d8d8d;
    width:50%;
  }
  
  .btn-password-recovery:hover {
    color:#4a4a4a;
    cursor:pointer;
  }
  
  .btn-yandex {
    display:flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 2vh;
    padding:.5vh 1vw;
    width:35%;
    color:#fff;
    font-family:Golos-Text;
    background-color: rgb(255,47,47);
  }
  
  .btn-yandex:hover {
    background-color: rgb(175, 34, 34);
    cursor:pointer;
  }
  
  .btn-google {
    display:flex;
    flex-direction: row;
    gap: 2vh;
    padding:.5vh 1vw;
    width:35%;
    color:#191919;
    background-color: rgb(255, 255, 255);
    border:1px solid #ececec;
    font-family:Golos-Text;
  }
  
  .btn-google:hover {
    background-color: rgb(232, 232, 232);
    cursor:pointer;
  }
  
  .text-btn {
    display: flex;
    align-items:center;
    font-family:Golos-Text;
    padding:0;
    font-size:1.4vh;
    margin:auto;
  }
  
  .icon-btn img {
    width:3vh;
    height:3vh;
  }
  
  .btn-go-register {
    cursor: pointer;
    display:none;
    flex-direction: row;
    gap: 2vh;
    border-radius: 2vh;
    padding:.7vh 3vh .2vh 1vh;
    border:2vh;
    color:#101010;
    background-color: rgb(236, 236, 236);
    margin-top:.5vh;
  }
  
  /* MEDIA */
  
  @media (max-width: 500px) {
    .box-password-recovery {
      padding-left:6vw;
    }
    .left-section {
      display: none;
    }
  
    .right-section {
      width: 100%;
    }
  
    .btn-wrapper {
      display: flex;
      flex-direction: column;
      row-gap: 10px;
      justify-content: center;
      align-items: center;
    }
    .window {
      width:90%;
      
    }
    .btn-reg {
      width:90%;
    }
  
    .btn-sign-in {
      width:90%;
    }
  
    .btn-go-register .text-btn {
      font-size:1.5vh;
    }
  
    .input-wrapper input {
      font-size:15px;
    }
  }
  
  @media (max-width: 1530px) {
  
  .btn-yandex .text-btn {
    font-size: 1.5vh;
  }
  }
  
  @media (max-width: 1380px) {
  
  .btn-yandex .text-btn {
    font-size: 1.4vh;
  }
  }
  
  @media (max-width: 1350px) {
    .left-section {
      width: 30%;
    }
  
    .right-section {
      width: 70%;
    }
    .btn-yandex {
      width:39%;
    }
    .btn-google {
      width:39%;
    }
    .btn-go-register .text-btn {
      font-size:1.5vh;
    }
  }
  
  
  
  @media (max-width: 1000px) {
    .left-section {
      display: none;
    }
  
    .right-section {
      width: 100%;
    }
  
    .btn-go-register .text-btn {
      font-size:1.5vh;
    }
    .btn-yandex {
      width:42%;
    }
    .btn-google {
      width:42%;
    }
  }
  
  .fast-auth-box {
    width:100%;
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap:.5vw;
  }
  .text-sign-in-bottom {
    padding-left:1.5vw;
    font-family:Golos-Text;
    font-size: 1.5vh;
  }
  
  .sign-in-botton-line {
    padding-top:3vh;
    display:flex;
    flex-direction: column;
    gap:.5vw;
    width:100%;
  }
    </style>
    