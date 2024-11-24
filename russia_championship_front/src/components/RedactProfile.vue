<template>
  <div class="window-change-profile">
    <div class="image-line">
      <img src="../assets/logo.png">
      <div class="line-btn-up">
      <div class="btn-mainpage" @click="this.$router.push('/info')">
        На главную
      </div>
      <div class="btn-profile" @click="this.$router.push('/profile')">
        <img src="../assets/profile-icon.png" >
      </div>
    </div>
    </div>
    <div class="main-info-line">
      <div class="left-side">
        <div class="profile-picture">
          <img :src="image_url" class="main-image" alt="Profile Picture">
        </div>
        <div class="image-redactor">
          <label class="file-input-label" for="file-upload" >Изменить фото</label>
          <!-- <label class="file-input-label" @click="handleFileUpload" v-if="image">Сохранить фото</label> -->
          <input 
            type="file" 
            id="file-upload" 
            class="file-input" 
            name="image" 
            @change="handleFileUpload"
          >
        </div>
      </div>
      <div class="right-side">
        <div class="main-info">
          <div class="value-name-now" id="text-info">
            {{ new_fio }}
          </div>
          <div class="value-number-now" id="meta-text-info" >
            Местоположение: {{ new_city }}
          </div>
          <div class="value-number-now" id="meta-text-info">
            Моб.телефон: {{ new_phone }}
          </div>
          <div class="value-mail-now" id="meta-text-info">
            Почтовый адрес: {{ email }}
          </div>
        </div>
      </div>
    </div>

    <div class="change-info-line">
      <div class="line-text">Редактировать данные</div>
        <div class="input-box">
          <label for="fio">ФИО</label>
          <input type="text" id="fio" v-model="fio" placeholder="Введите ФИО" required />
        </div>
        <!-- <div class="input-box">
          <label for="fullName">Дата рождения</label>
          <input type="text" id="fullName" v-model="birthday_date" placeholder="Введите дату рождения" required />
        </div> -->
        <div class="input-box">
          <label for="phone">Телефон</label>
          <input type="tel" id="phone" v-model="phone"  placeholder="Введите свой номер телефона" required />
        </div>
        <div class="input-box">
          <label for="city">Город</label>
          <input type="text" id="city" v-model="city"  placeholder="Москва" />
        </div>
        <!-- <div class="input-box">
          <label for="email">Почта</label>
          <input type="email" id="email" v-model="email" placeholder="asd" required />
        </div> -->
        <div class="input-box">
          <label for="line-textarea">О себе</label>
          <div class="line-textarea">
            <textarea v-model="description" rows="5" placeholder="Напишите о себе"></textarea>
        </div>
        </div>
      <div class="btns-line">
      <div class="btn-line">
        <button id="btn-change" class="btn-change-info" @click="commitChange">Сохранить изменения</button>
      </div>
      <br>
      <div class="btn-line">
        <button id="btn-change" class="btn-change-password" @click="changePassword">Изменить пароль</button>
      </div>
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
        phone: '',
        image : null,
        trainer : false,
        fio : '',
        email : 'не указан',
        description : '',
        city : '',
        new_city : 'Не указано',
        birthday_date : '',
        new_fio : 'Не указано',
        new_phone : 'Не указан',
        image_url : 'https://storage.yandexcloud.net/step2002sharp/none-profile.png',
        cities : []
      };
    },

    methods: {

      PhotoChanged(event){
        this.image = event.target.files[0];
        if (this.image) {
          this.image_url = URL.createObjectURL(this.image); // Предпросмотр изображения
        }
      },
      changePassword(){
        this.$router.push('/user/changepass')
      },
      async commitChange(){
        console.log(typeof this.phone);
        
        const response = await axios.patch('/api/user/change/profile', {
          // birthday_date: this.birthday_date,
          FIO : this.fio,
          is_coach : this.trainer,
          phone_number:this.phone,
          about : this.description,
        });
        
        if (!response.data) {
          eventBus.emit('show-modal', 'Ошибка при сохранении данных, повторите попытку позже');
          return 0
        }
        this.new_fio = this.fio
        this.new_phone= this.phone
        this.new_city= this.city
        eventBus.emit('show-modal', 'Данные успешно изменены');
        
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
        const file = event.target.files[0]; 
        if (!file) return;
        this.image = file;


        const reader = new FileReader();
        reader.onload = (event) => {
          this.image_url = event.target.result;
        };
        reader.readAsDataURL(file);
        this.uploadPhoto()
      },

      async uploadPhoto() {
        try {
            const formData = new FormData();
            formData.append('file', this.image);
            const response = await axios.post('/api/images/add_profile_image_to_s3', formData, {
              headers: {
                'Content-Type': 'multipart/form-data',
              },
            });
            
            eventBus.emit('show-modal', 'Фото успешно загружено');
          } catch (error) {
            console.log(error);
            
            eventBus.emit('show-modal', 'Ошибка при загрузке фотографии');
          }
        },
      
    },
    async mounted(){
      try {
          this.cities = (await axios.get('/api/events/all_city')).data
          const user = await axios.get('/api/user/profile/me')
        if (user.data.User.birthday_date !==null) {//about
          this.birthday_date = user.data.User.birthday_date
        }
        if (user.data.User.about !==null) {//about
          this.description = user.data.User.about
        }
        if (user.data.User.phone_number !=="") {//phone
          this.phone = user.data.User.phone_number
          this.new_phone = this.phone
        }
        try {
          if (user.data.User.city.city_name !==null) {//city
          this.city = user.data.User.city.city_name
          this.new_city = this.city
        }
        } catch (error) {
          
        }
        if (user.data.User.fio !==null) {//fio
          this.fio = user.data.User.FIO
          this.new_fio = this.fio
        }
        this.trainer = user.data.User.is_coach,
        this.email = user.data.User.email

      } catch (error) {
        console.log(error);
        eventBus.emit('show-modal', 'Авторизуйтесь и поворить попытку');
      }

      
      try {
        const url = await (await axios.get('/api/images/get_url_image_profile_from_s3')).data
        this.image_url = url 
      } catch (error) {
        console.log(error);
        eventBus.emit('show-modal', 'Ошибка при изменени фото, попробуйте позже');
      }
      
    }
  };
  </script>
  
  
  <style scoped>

  .window-change-profile {
    background-color: rgb(255, 255, 255);
    height:130vh;
    width:50%;
    -webkit-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    -moz-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    display:flex;
    flex-direction: column;
  }

  .image-line {
    height:10%;
    background-color: rgb(49,68,104);
    background-repeat: no-repeat;
    width:100%;
    background-size: cover;
    display:flex;
    align-items: center;
    justify-content: space-between;
  }

  .image-line img {
    width:60px;
    margin-left:2vw;
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
    width:250px;
    height:250px;
    border-radius: 100%;
    overflow: hidden;
  }


  .main-info-line .right-side {
    height:100%;
    width:60%;
    display:flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    padding-top:8vh;
  }

  .main-info {
    display:flex;
    flex-direction: column;
    gap:1vh;
    width:90%;
    overflow: hidden;
  }

  .value-name-now {
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:35px;
    font-weight: 600;
    font-family: Golos-Text;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-city-now {
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Golos-Text;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-number-now {
    width:100%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Golos-Text;
    overflow: hidden;
    white-space:nowrap;
  }

  .value-mail-now {
    width:90%;
    display:flex;
    justify-content: left;
    align-items: center;
    font-size:17px;
    font-family: Golos-Text;
    overflow: hidden;
    white-space:nowrap;
  }

  .change-info-line {
    width:100%;
    height:35%;
    display:flex;
    flex-direction: column;
    gap:1.5vh;
  }
  .line-text {
    height:20%;
    font-size: 30px;
    font-family: Golos-Text;
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

.input-box {
    width:100%;
    height:5vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height:9vh;
  }

  .input-box label {
    font-size: 17px;
    font-family: Golos-Text;
    color: #101010;
    width:20vw;
    height:2vh;
    display:flex;
    justify-content: start;
    align-items: end;
    padding:.5vh 0;
  }
  .input-box input {
    font-size: 17px;
    font-family: Golos-Text;
    border:1px solid #eaeaea;
    background-color: #eaeaea;
    border-radius: .5vh;
    outline:0;
    padding:0 1vh;
    height:4vh;
    width:19vw;
  }

  .btn-line {
    display:flex;
    justify-content: center;
    align-items: center;
  }

  .btn-change-info {
    width:20vw;
    height:4vh;
    font-size:1.7vh;
    background-color: rgb(49,68,104);
    color:#fff;
    border:none;
    cursor: pointer;
    font-family: Golos-Text;
  }

  .btn-change-password {
    width:20vw;
    height:4vh;
    font-size:1.7vh;
    background-color: rgb(255, 255, 255);
    border:1px solid rgb(49,68,104);
    color:rgb(49,68,104);
    cursor: pointer;
    font-family: Golos-Text;
  }

  .btn-change-password:hover {
    background-color: rgb(111, 141, 198);
    border:1px solid rgb(111, 141, 198);
    color:#fff;
  }

  .btn-change-info:hover {
    background-color: rgb(32,44,67);
  }

  .btn-mainpage {
    background-color: rgb(255, 255, 255);
    height:4vh;
    display:flex;
    justify-content: center;
    align-items: center;
    padding:0 2vw;
    font-family: Golos-Text-Semibold;
    cursor: pointer;
    border-radius: .5vh;
  }
  .btn-mainpage:hover {
    background-color: rgb(228, 228, 228);
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
    font-family: Golos-Text;
    font-weight:600;
  }

  .line-textarea {
    display:flex;
    justify-content: center;
    width:20vw;
  }

  .line-textarea textarea {
    width:100%;
    border:1px solid #eaeaea;
    outline:0;
    background-color: #eaeaea;
    padding:0 .5vw;
    font-family:Golos-Text;
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
  .file-input-container {
      overflow: hidden;
      position: relative;
    }
    
    .file-input-label {
      background: rgb(49,68,104);
      padding: 1vh 3vh;
      cursor: pointer;
      display:flex;
      justify-content: center;
      align-items: center;
      font-family: Golos-Text;
      font-size:1.7vh;
      border: 1px solid #d3d3d3;
      color:#fff;
      width:10vw;
    }

    .file-input-label:hover {
      background-color: rgb(32,44,67);
    } 

    .image-redactor {
      display:flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      gap:.5vw;
      width:100%;
      height:20%;
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

    .btns-line {
      display: flex;
      flex-direction: column;
      gap:0;
      margin-top:2vh;
    }
    .line-btn-up {
      display:flex;
      flex-direction: row;
      padding-right:2vw;
      gap:1vw;
    }

    .btn-profile {
      background-color: #fff;
      display:flex;
      justify-content: center;
      align-items: center;
      width:2vw;
      height:4vh;
      cursor: pointer;
      border-radius: .5vh;
    }

    .btn-profile:hover {
      background-color: #e3e3e3;
    }

    .btn-profile img {
      width:.75vw;
      height:1.4vh;
      margin: auto;
      filter:invert(.5)
    }
  </style>
  