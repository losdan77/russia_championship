<template>
  <div class="window-change-profile">
    <div class="image-line">

    </div>

    <div class="main-info-line">
      <div class="left-side">
          <div class="profile-picture">
            <img src="https://via.placeholder.com/100" alt="Profile Picture" class="main-image">
          </div>
          <div class="image-redactor">
            <input type="file" id="fileupload" name="image" @change="handleFileUpload" v-if="!image">
            <button v-if="image">Добавить</button>
          </div>
      </div>
      <div class="right-side">
        <div class="value-name-now" id="text-info">
          {{ fullName }}
        </div>
        <div class="value-number-now" id="meta-text-info" >
          Местоположение: {{ city }}
        </div>
        <div class="value-number-now" id="meta-text-info">
          Моб.телефон: {{ phone }}
        </div>
        <div class="value-mail-now" id="meta-text-info">
          Почт.адрес: {{ email }}
        </div>
      </div>
    </div>

    <div class="change-info-line">
      <div class="line-text">Редактировать данные</div>
      <div class="line-input" id="up-line">
        <div class="input-box">
          <label for="fullName">ФИО</label>
          <input type="text" id="fullName" v-model="fullName" placeholder="Иванов Иван" required />
        </div>
        <div class="input-box">
          <label for="phone">Телефон</label>
          <input type="tel" id="phone" v-model="phone"  placeholder="+7(999)-999-99-99" required />
        </div>
      </div>
      <div class="line-input" id="down-line">
        <div class="input-box">
          <label for="city">Город</label>
          <input type="text" id="city" v-model="city"  placeholder="Москва" />
        </div>
        <div class="input-box">
          <label for="email">Почта</label>
          <input type="email" id="email" v-model="email" placeholder="asd" required />
        </div>
      </div>
      <div class="description-line">
        <div class="text-discription">Редактировать "О себе"</div>
        <div class="line-textarea">
          <textarea v-model="aboutMe" rows="5" placeholder="Напишите о себе..."></textarea>
        </div>
      </div>
      <div class="btn-line">
        <button id="btn-change" class="btn-change-info" @click="commitChange">Сохранить изменения</button>
      </div>
      <br>
      <div class="btn-line">
        <button id="btn-change" class="btn-change-info" @click="changePassword">Изменить пароль</button>
      </div>
    </div>


  </div>
  </template>
  
  
  <script>
import axios from 'axios';
import eventBus from '../eventBus';

  export default {
    data() {
      return {
        fullName: 'Иван Иванов',
        phone: '+7 (999) 999-99-99',
        rating: 4.5,
        city: 'Kaspersk',
        email: 'lossdan@asd',
        aboutMe: '♥',
        image : null,
        birthday_date : ''
      };
    },

    methods: {
      changePassword(){
        this.$router.push('/user/changepass')
      },
      async commitChange(){
        const response = await axios.post('/api/user/registr', {
          birthday_date: this.birthday_date,
          FIO : this.fullName,
          is_coach : this.trainer,
          phone_number:this.phone,
          about : this.aboutMe
        });
        console.log(response);
        if (!response.data) {
          eventBus.emit('show-modal', 'Jib,rf');
          return 0
        }
        eventBus.emit('show-modal', 'Вы успешно зарегистрировались');
        this.$router.push('/auth')
        
      },
      async submitForm() {
        try {
          const formData = new FormData();
          formData.append('image', this.image);
        } catch (error) {
          console.error('Ошибка при отправке данных:', error.response.data);
        }
      },
      handleFileUpload(event) {
        this.image = event.target.files[0];
      },
    }
  };
  </script>
  
  
  <style scoped>

  .window-change-profile {
    position:absolute;
    left:0;
    right:0;
    top:0;
    bottom:0;
    margin:auto;
    background-color: rgb(255, 255, 255);
    height:80%;
    width:50%;
    -webkit-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    display:flex;
    flex-direction: column;
  }

  .image-line {
    height:10%;
    background: url('..//assets/fon.PNG');
    background-repeat: no-repeat;
    width:100%;
    background-size: cover;
  }

  .main-info-line {
    display:flex;
    flex-direction: row;
    height:30%;
    width:100%;
    padding-bottom: 2% ;
  }

  .main-info-line .left-side {
    height:100%;
    width:40%;
    display:flex;
    flex-direction: column;
  }

  .profile-picture {
    display:flex;
    justify-content: center;
    align-items: center;
    height:90%;;
  }

  .profile-picture img {
    width:150px;
    height:150px;
    border-radius: 100%;
    overflow: hidden;
  }

  .image-redactor {
    height:10%;
    display:flex;
    justify-content: center;
    align-items: center;
  }

  .main-info-line .right-side {
    height:100%;
    width:60%;
    display:flex;
    flex-direction: column;
  }

  .value-name-now {
    height:55%;
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:35px;
    font-weight: 600;
    font-family: Arial, Helvetica, sans-serif;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-city-now {
    height:15%;
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Arial, Helvetica, sans-serif;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-number-now {
    height:15%;
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Arial, Helvetica, sans-serif;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-mail-now {
    height:15%;
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Arial, Helvetica, sans-serif;
    overflow: hidden;
    white-space:nowrap;
  }

  .change-info-line {
    width:100%;
    height:35%;
    
    display:flex;
    flex-direction: column;
  }
  .line-text {
    height:20%;
    font-size: 30px;
    font-family: Arial, Helvetica, sans-serif;
    padding-left: 7%;
    font-weight: 600;
    display:flex;
    align-items: center;
  }
  .change-info-line .line-input {
    height:25%;
    width:100%;
    display:flex;
    flex-direction: row;
  }

  .line-input .input-box {
    width:50%;
    height:100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
    padding-left: 7%;
  }

  .input-box label {
    width:80%;
    font-size: 17px;
    font-family: Arial, Helvetica, sans-serif;
    color: #a1a1a1;
  }
  .input-box input {
    width:80%;
    font-size: 17px;
    height:50%;
    font-family: Arial, Helvetica, sans-serif;
    border:1px solid #eaeaea;
    background-color: #eaeaea;
    border-radius: .5vh;
    outline:0;
    padding-left:5%;
  }

  .btn-line {
    width:93%;
    height:20%;
    padding-left:7%;
    display:flex;
    justify-content: start;
    align-items:end;
  }

  .btn-change-info {
    height:40px;
    background-color: rgb(42, 42, 42);
    color:#fff;
    border:none;
    padding: 0 2%;
    cursor: pointer;
  }

 
  .description-line {
    height: 50%;
    display: flex;
    flex-direction: column;
    gap:2%;
  }

  .text-discription {
    height:20%;
    font-size:20px;
    padding-left:7%;
    font-family: Arial, Helvetica, sans-serif;
    font-weight:600;
  }

  .line-textarea {
    height:50%;
    display:flex;
    justify-content: center;
  }

  .line-textarea textarea {
    width:83%;
    height:80%;
    border:1px solid #eaeaea;
    outline:0;
    background-color: #eaeaea;
    padding-left:2%;
  }

  .btn-line-1 {
    width:93%;
    height:fit-content;
    padding-left:7%;
    display:flex;
    justify-content: start;
    align-items:start;
  }

  .btn-change-description {
    height:90%;
    background-color: rgb(42, 42, 42);
    color:#fff;
    border:none;
    padding: 0 2%;
  }

  @media (max-width:1350px) {
    #text-info {
      font-size: 30px;
    }

    #meta-text-info {
      font-size: 14px;
    }
    .line-text {
      font-size: 25px;
    }

    .input-box label {
      font-size: 13px;
    }
    .image-redactor input {
      width:70%;
    }
    .profile-picture img {
    width:125px;
    height:125px;
    }
  }

  @media (max-width:900px) {
    #text-info {
      font-size: 25px;
    }

    #meta-text-info {
      font-size: 12px;
    }
    .line-text {
      font-size: 20px;
    }

    .input-box label {
      font-size: 10px;
    }
    .image-redactor input {
      width:65%;
    }
    .profile-picture img {
    width:100px;
    height:100px;
    }

    .input-box input {
      height:50%;
      font-size: 12px;
    }

    .btn-line button {
      height:50%;
      font-size:10px;
    }

    .btn-line-1 button {
      height:70%;
      font-size:10px;
    }

    .window-change-profile {
      width: 50%;
    }

  }

  @media (max-width:700px) {
    #text-info {
      font-size: 20px;
    }

    #meta-text-info {
      font-size: 10px;
    }
    .line-text {
      font-size: 16px;
    }

    .input-box label {
      font-size: 10px;
    }
    .image-redactor input {
      width:65%;
    }
    .profile-picture img {
    width:75px;
    height:75px;
    }

    .input-box input {
      height:40%;
      width:70%;
      font-size: 10px;
    }

    .btn-line button {
      height:50%;
      font-size:10px;
    }

    .btn-line-1 button {
      height:70%;
      font-size:10px;
    }

    .window-change-profile {
      width: 80%;
    }
    .text-discription {
      font-size: 14px;
     }

  }

  @media (max-width:450px) {
    .window-change-profile {
      width: 90%;
      height: 95%;
    }
    .main-info-line {
      width:100%;
      flex-direction: column;
      align-items: center;
    }

    .left-side {
      width:100%;
      height:50%;
    }

    .right-side {
      width:100%;
      height:50%;
      align-items: center;
    }
    
    .value-name-now {
      justify-content: center;
    }
    
    .value-city-now {
      justify-content: center;
    }
    
    .value-number-now {
      justify-content: center;
    }
    
    .value-mail-now {
      justify-content: center;
    }

    .change-info-line {
      align-items: center;
    }

    .change-info-line .line-input { 
      flex-direction: column;
      width:70%;
    }

    .line-input .input-box {
      width:90%;
      justify-content: left;
    }

    .input-box input {
      width:90%;
      height:85%;
    }

    .btn-line {
      width:100%;
      padding-left:0;
      justify-content: center;
    }

    .btn-line-1 {
      width:100%;
      padding-left:0;
      justify-content: center;
    }

    #text-info {
      font-size: 20px;
    }

    #meta-text-info {
      font-size: 10px;
    }
    .line-text {
      font-size: 16px;
    }

    .input-box label {
      font-size: 10px;
    }
    .image-redactor input {
      width:65%;
    }
    .profile-picture img {
    width:75px;
    height:75px;
    }


    .btn-line button {
      height:50%;
      font-size:10px;
    }

    .btn-line-1 button {
      height:70%;
      font-size:10px;
    }

    .window-change-profile {
      width: 80%;
    }
    .text-discription {
      font-size: 14px;
     }

  }
  </style>
  