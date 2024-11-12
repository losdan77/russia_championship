<template>
<div class="window">
    <section class="left-section">
      <div class="section" id="section-1">
        <div class="content-section-1">
          <div class="logo-img">
            <img src="../assets/yandex.png" @click="goToHome"/>
          </div>
          <div class="btn-reg" @click="GoToReg()">Создать аккаунт</div>
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
        <div class="btn-wrapper">
          <div class="btn-password-recovery" @click="GoToRestoring">Забыли пароль?</div>
          <div class="btn-sign-in" @click="Authorization()">Войти</div>
        </div>
        <div class="yandex-wrapper">
          <div class="btn-yandex">
            <div class="icon-btn">
              <img src="../assets/yandex.png">
            </div>
            <div class="text-btn"  
            @click="openWindow"
            >
            Войти через Гугл
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
    <!-- <div class="login-page">
      <h1>Вход</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <p @click="GoToReg()" class="GoToReg">У меня нет аккаунта</p>
        <button type="submit" class="login-button" @click="Authorization()">Войти</button>
      </form>
    </div> -->
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
      onLoginClick() {
        
        console.log('Кнопка авторизации нажата');
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
        if (response) {
          eventBus.emit('show-modal', 'Вы успешно авторизованы');
          this.$router.push('/profile')
        }
        } catch (error) {
          eventBus.emit('show-modal', 'Неправильный Email или пароль');
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
        const newWindow = window.open(url.data, '_blank');
        if (newWindow) {
          newWindow.blur();
        }
        window.open('http://localhost:5173/', '_self');
      }
    },
    // goToHome(){
    //   this.$router.push('/')
    // },
    created() {

    const urlParams = new URLSearchParams(window.location.search);
    this.code = urlParams.get('code'); // Извлекаем 'code'

    if (this.code) {
      // Если код есть, отправляем его на сервер для получения токена
      this.exchangeCodeForToken();

      
    }
  },
  };
  </script>
  
  <style scoped>

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
  top:0;
  bottom:0;
  left:0;
  right:0;
  margin:auto;
  text-align: center;
  align-content: center;
}

.logo-img img {
  width:3vw;
  height:3vw;
}
.btn-reg {
  position: absolute;
  width:15vw;
  height:4vh;
  top:29.5vh;
  bottom:0;
  left:0;
  right:0;
  margin:auto;
  text-align: center;
  align-content: center;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 700;
  border-radius: 2vh;
  color:#fff;
  background-color: #9db5b4a6;
}

.btn-reg:hover {
  background-color: #73808597;
  cursor:pointer;
  transition: all .4s ease;
}

.upper-wrapper {
  padding:3vh 0 0 3vh;
  height:4vh;
  font-size:3vh;
  font-family: Arial, Helvetica, sans-serif;
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
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f0f0f0;
}

.input-wrapper input {
  background-color: #f0f0f0;
  outline: 0;
  border:0;
  height:3vh;
  padding-left:3.5vh;
  font-size: 1.8vh;
  font-family: Arial, Helvetica, sans-serif;
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
  padding: 1vh 3vh;
}

.btn-sign-in {
  display: flex;
  background-color: #333;
  font-size:2vh;
  align-items: center;
  justify-content: center;
  padding: .5vh 5vh;
  height:4vh;
  border-radius: 3vh;
  font-family: Arial, Helvetica, sans-serif;
  color:#fff;
}

.btn-sign-in:hover {
  background-color: #bfbfbf;
  cursor:pointer;
}

.btn-password-recovery {
  font-size:1.6vh;
  font-family: Arial, Helvetica, sans-serif;
  display: flex;
  justify-content: left;
  align-items: center;
  color:#8d8d8d;
}

.btn-password-recovery:hover {
  color:#4a4a4a;
  cursor:pointer;
}

.yandex-wrapper {
  padding:5vh 3vh 1vh 3vh;
}

.btn-yandex {
  display:flex;
  flex-direction: row;
  gap: 2vh;
  border-radius: 2vh;
  padding:.7vh 3vh .2vh 1vh;
  border:2vh;
  color:#fff;
  background-color: rgb(255,47,47);
}

.btn-yandex:hover {
  background-color: rgb(175, 34, 34);
  cursor:pointer;
}

.text-btn {
  display: flex;
  align-items:center;
  font-family: Arial, Helvetica, sans-serif;
  padding:0;
  font-size: 1.8vh;
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
  .left-section {
    display: none;
  }

  .right-section {
    width: 100%;
  }

  .btn-wrapper {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
  .window {
    width:80%;
    
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

  .btn-reg {
    display: none;
  }

  .btn-go-register {
    display:flex;
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

}


  </style>
  