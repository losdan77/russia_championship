<template>

  <div class="window">
    <section class="left-section">
      <div class="section" id="section-1">
        <div class="content-section-1">
        </div>
      </div>
    </section>
    
    <section class="right-section">
      <div class="section" id="section-2">
        <div class="upper-wrapper">
          Регистрация
        </div>
        <div class="select-wrapper">
          <div class="type-selector">
          <div 
            :class="['selector-option1', { 'active': userType === 'individual' }]" 
            @click="setUserType('individual')"
          >
            Спортсмен
          </div>
          <div 
            :class="['selector-option2', { 'active': userType === 'organization' }]" 
            @click="setUserType('organization')"
          >
            Тренер
          </div>
        </div>
        </div>
        <div class="input-wrapper">
          <div class="wrapper-input">
          <label for="fullName">ФИО (необязательно)</label>
          <input type="text" id="fullName" v-model="fullName" required />
        </div>
        <div class="line-wrapper">
        <div class="wrapper-input">
          <label for="email">Почта*</label>
          <input type="email" id="email" v-model="email" required />
        </div>


        <div class="wrapper-input">
          <label for="password">Пароль* (не менее 5 символов)</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="wrapper-input">
          <label for="confirm-password">Подтвердите пароль*</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
        </div>
        <div class="form-row">
          <div class="wrapper-input" id="nubmer-phone">
            <label for="phone">Номер телефона (необязательно)</label>
            <input type="tel" id="phone" v-model="phone" required />
          </div>
          <div class="wrapper-input" id="city-user">
            <label for="city">Город (необязательно)</label>
            <input type="text" id="city" v-model="city" />
          </div>
        </div>


        <!-- <div class="wrapper-input" id="photo-wrapper">
          <div class="image-redactor">
            <div class="text-image-redactor">Фото профиля (необязательно)</div>
            <div class="top-line-photo">
            <div class="">
            <label class="file-input-label" for="file-upload">Загрузить фото</label>
            <input type="file" id="file-upload" class="file-input" name="image" @change="handleFileUpload" v-if="!image">
          </div>
            <button v-if="image" @click="AddPhoto" class="save-button">Добавить</button>
            </div>
          </div>
          </div> -->
        <div type="submit" class="register-button" @click="Register()">Зарегистрироваться</div>
        <p @click="GoToLogin()" class="GoToLogin">У меня уже есть аккаунт</p>
        <div class="logo-pic">
          <img src="../assets/logo.png"/>
        </div>
        <div class="line-btn">
          <div class="btn-exit" @click="goToPrimary">Вернуться</div>
        </div>
        </div>
      </div>
      </div>
    </section>

  </div>
    
  </template>

  
  <script>
import axios from 'axios'
import eventBus from '../eventBus';

export default {
    data() {
      return {
        userType: 'individual',
        fullName: '',
        email: '',
        phone: '',
        city: '',
        trainer: false,
        govNumber: '',
        password: '',
        confirmPassword: '',
        image: null,
        image_url: null,
      };
    },
    methods: {
      goToPrimary() {
        this.$router.push('/')
      },
      setUserType(type) {
        this.userType = type;
        if (this.organizationType === 'organization') {
          this.trainer = true
        }
      },
      GoToLogin(){
        this.$router.push('/auth')
      },
      async Register(){
        try {
        this.submitForm()
          const response = await axios.post('/api/user/registr', {
            email: this.email,
            password: this.password,
            password_verify: this.confirmPassword,
            is_coach : this.trainer,
            phone_number:this.phone,
            photo_url : this.image_url,
            city : this.city,
            FIO : this.fullName
          });
          eventBus.emit('show-modal', 'Вы успешно зарегистрировались');
          this.$router.push('/auth')
        } catch (error) {
          console.log(error);
          if (error.response.status == 422) {
            eventBus.emit('show-modal', 'Пропущенно одно или несколько обязательных полей');
          return 0
          }
          if (error.response.status == 401) {
            eventBus.emit('show-modal', 'Такой пользователь уже есть');
          return 0
          }
          eventBus.emit('show-modal', 'Ошибка при регистрации');
        }
      },
      // handleFileUpload(event) {
      //   this.image = event.target.files[0];
      //   if (this.image) {
      //     this.image_url = URL.createObjectURL(this.image); // Предпросмотр изображения
      //   }
      // },
      submitForm() {
        if (this.password !== this.confirmPassword) {
          eventBus.emit('show-modal', 'Пароли не совпадают');
          return 0
        } 
      },
      // async AddPhoto(){
      //   try {
      //     const id = this.$route.params.id
      //     const formData = new FormData();
      //     formData.append('file', this.image);
      //     console.log(this.image);
      //     const response = await axios.post(`/api/images/add_profile_image_to_s3?id_profile=${id}`, formData, {
      //       headers: {
      //         // 'Content-Type': 'multipart/form-data'
      //       }
      //   });
      //   const image_url = await axios.get(`/api/imagesget_url_image_profile_from_s3?id_profile=${id}`)
      //   this.image_url = image_url.data
      //   console.log(image_url.data);
        

      //   } catch (error) {
      //     console.log(error);
      //     eventBus.emit('show-modal', 'Ошибка при добавлении фото, попробуйте позже');
      //   }
      //   alert("Добавить фото")
      // }
    }
  };
  </script>
  
  <style scoped>

  .window {
  display: flex;
    width: 50%;
    height:80%;
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
    width: 30%;
    background-color: #f0f0f0;
  }
  
  .right-section {
    width: 70%;
    border: 1px solid #f5f5f5;
    background-color: #ffffff;
  }
  
  .section {
    background-color: #ffffff;
    display:flex;
    flex-direction: column;
    width:100%;
    height:100%;
  }
  
  #section-1 {
    background: url('../assets/fon2.png');
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
    background-color: #33333375;
    width:9vw;
    height:9vw;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .profile-picture {
    width:100%;
    height:100%;
  }
  
  .profile-picture img {
    width:100%;
    height:100%;
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
    padding-top:1vw;
    padding: 1vw 3vh 2vh 3vh;
  }
  
  .input-wrapper label {
    height:1.5vh;
    padding-left:3vh;
    padding-top:.5vh;
    font-size: 1.3vh;
    color:#919191;
    font-family: Golos-Text;
    background-color: #f0f0f0;
    overflow: hidden;
  }
  
  .input-wrapper input {
    background-color: #f0f0f0;
    outline: 0;
    border:0;
    height:2.5vh;
    padding-left:3.5vh;
    font-size: 1.8vh;
    font-family: Golos-Text;
    cursor:pointer;
  }
  
  .input-wrapper select {
    background-color: #f0f0f0;
    outline: 0;
    border:0;
    height:2.5vh;
    padding-left:3.5vh;
    font-size: 1.5vh;
    font-family: Golos-Text;
    cursor:pointer;
    overflow: hidden;
    width:100%;
  }
  .type-selector {
      display: flex;
      justify-content: center;
      margin-bottom: 1vw;
    }
  
    
    .selector-option2 {
      flex: 1;
      text-align: center;
      padding: 10px;
      cursor: pointer;
      background-color: #f5f5f5;
      transition: background-color .6s ease;
      
      font-family: Golos-Text;
      color:#9d9d9d
    }
    .selector-option1 {
      flex: 1;
      text-align: center;
      padding: 10px;
      cursor: pointer;
      transition: background-color .6s ease;
      font-family: Golos-Text;
      color:#9d9d9d
    }
    
    .selector-option1.active {
      background-color: rgb(49,68,104);
      color: #fff;
      border-color: #333;
      font-weight: bold;
    }
    
    .selector-option1:not(.active):hover {
      background-color: #eee;
      
    }
    .selector-option2.active {
      background-color: rgb(49,68,104);
      color: #fff;
      border-color: #333;
      font-weight: bold;
    }
    
    .selector-option2:not(.active):hover {
      background-color: #eee;
    }
  
    .wrapper-input {
    display:flex;
    flex-direction: column;
    margin-top:1vh;
    border-bottom:1px solid #eeeeee;
  }
  
  .wrapper-input:hover {
    transition: all .4s ease;
    border-bottom:1px solid #9d9d9d;
    cursor:pointer;
  }
  .form-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  #nubmer-phone {
    width:57%;
  }
  #type-org {
    width:57%;
  }
  .select-wrapper {
    padding: 3vh 3vh 0 3vh;
  }
  .register-button {
    display: flex;
    background-color: rgb(49,68,104);
    font-size:2vh;
    align-items: center;
    justify-content: center;
    padding: .5vh 5vh;
    height:4vh;
    border-radius: 0vh;
    font-family: Golos-Text;
    color:#fff;
    transition: all .4s ease;
    margin-top:1vw;
  }
  
  .register-button:hover {
    background-color: rgb(33,44,67);
    cursor:pointer;
  }
  
  p {
    font-family: Golos-Text;
    color:#919191;
    transition: all .4s ease;
  }
  
  p:hover {
    color:#1d1d1d;
    cursor: pointer;
  }
  
  .save-button {
    background-color: #333;
    color:#fff;
    border:0;
    display:flex;
    justify-content: center;
    align-items: center;
    cursor:pointer;
    font-family: Golos-Text-Semibold;
  } 
  .save-button:hover {
    background-color: #3e3e3e;
  }
  .logo-pic {
    display: flex;
    justify-content: center;
  }
  
  .logo-pic img {
    width:40px;
    height:40px;
    filter: invert(1);
  }
  #photo-wrapper {
    border:0;
  }
  #photo-wrapper:hover {
    border:0;
  }
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
      width:100%;
      height:100%;
    }s
    .register-button {
      margin-top:2vw;
    }
    .btn-go-register .text-btn {
      font-size:1.5vh;
    }
    .input-wrapper input {
      font-size:15px;
    }
    #type-org {
      width:49%;
    }
    #gos-num {
      width:49%;
    }
    #nubmer-phone {
      width:49%;
    }
    #city-user {
      width:49%;
    }
    p {
      font-size:1.4vh;
    }
  }
  
  
  @media (max-width: 1600px) {
  
  .btn-yandex .text-btn {
    font-size: 1.5vh;
  }
  #type-org {
      width:49%;
    }
    #gos-num {
      width:49%;
    }
    #nubmer-phone {
      width:49%;
    }
    #city-user {
      width:49%;
    }
    p {
      font-size:1.7vh;
    }
    .save-button {
      font-size:1.5vh;
    }
  }
  
  @media (max-width: 1380px) {
  
  .btn-yandex .text-btn {
    font-size: 1.4vh;
  }
  #type-org {
      width:49%;
    }
    #gos-num {
      width:49%;
    }
    #nubmer-phone {
      width:49%;
    }
    #city-user {
      width:49%;
    }
    p {
      font-size:1.6vh;
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
    #type-org {
      width:49%;
    }
    #gos-num {
      width:49%;
    }
    #nubmer-phone {
      width:49%;
    }
    #city-user {
      width:49%;
    }
    p {
      font-size:1.6vh;
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
    #type-org {
      width:49%;
    }
    #gos-num {
      width:49%;
    }
    #nubmer-phone {
      width:49%;
    }
    #city-user {
      width:49%;
    }
    p {
      font-size:1.5vh;
    }
  }
  
  #fileupload {
    width:100%;
    padding:1vh 0;
  }
  
  .file-input-container {
      overflow: hidden;
      position: relative;
      
    }
    
    .file-input-label {
      background: #f0f0f0;
      padding: 1vh 3vh;
      cursor: pointer;
      display:flex;
      justify-content: center;
      align-items: center;
      border-radius: 5px;
      border: 1px solid #d3d3d3;
      width:10vw;
    }
    .image-redactor {
      display:flex;
      align-items: start;
      flex-direction: column;
      gap:.5vw;
      width:100%;
    }
    .file-input {
      width: 0.1px;
      height: 0.1px;
      opacity: 0;
      position: absolute;
      z-index: -1;
    }
    .text-image-redactor {
      font-size:1.4vh;
      display:flex;
      justify-content: center;
      align-items: center;
      font-family:Golos-Text;
    }
  
    .top-line-photo {
      display:flex;
      flex-direction: row;
    }

    .line-btn {
      width:100%;
      height:30%;
      display:flex;
      justify-content: end;
      align-items: end;
    }

    .btn-exit {
      background-color: #ffffff;
      color:#111111;
      border:1px solid #3e3e3e;
      display: flex;
      justify-content: center;
      align-items: center;
      padding:0 2vw;
      height:4vh;
      border-radius: 10px;
      font-family: Golos-Text;
    }

    .btn-exit:hover {
      background-color: #3e3e3e;
      cursor:pointer;
      color:#fff;
      transition:all .4s ease;
    }
    </style>
    