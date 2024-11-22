<template>
    <div class="window-view-profile">
      <div class="profile-photo">
        <div class="photo">
          <img src="..//assets/photo-profile.jpg">
        </div>
      </div>
      <div class="profile-content">
        <div class="content-line" id="city">
          <div class="tabs">
            <div class="tab" id="name-city">
              <img src="..//assets/marker.png">
              <div class="text-tab">{{ city }}</div>
            </div>
            <div class="tab" id="name-city">
              <img src="..//assets/marker.png">
              <div class="text-tab">{{birthday_date}}</div>
            </div>
  
            <div class="tab" id="name-status">
              <div class="text-tab" v-if="trainer">Тренер</div>
              <div class="text-tab" v-if="!trainer">Спортсмен</div>
            </div>

          </div>
        </div>
        <div class="content-line" id="username">
          <div class="text-username">{{ fio }}</div>
        </div>
        <div class="content-line" id="feedback">
          <div class="tabs">
            <div class="tab" id="feedback-tab">
              <img src="..//assets/phone.png">
              <div class="text-tab" >{{ phone }}</div>

            </div>
            <div class="tab" id="feedback-tab">
              <img src="..//assets/mail.png">
              <div class="text-tab">{{ email }}</div>
            </div>
          </div>
        </div>
        <div class="content-line" id="decription">
          <div class="left-content">
            <div class="text-description">
              {{ description }}
              
            </div>
          </div>
          <div class="right-content">
            <div id="tabs-description">

            <div class="tab" id="edit-tab" @click="goTOChangeProfile">
              <img src="..//assets/profile.png">
              <div class="text-tab" >Редактировать профиль</div>
            </div>
          </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data(){
      return {
        trainer : false,
        fio : 'Ваши данные пока что не указаны',
        email : '',
        description : 'Добавьте описание к своему профилю, свои достижения и список наград)',
        phone : 'Телефон е привязан к аккаунту',
        city : 'Ваш город не указан',
        birthday_date : 'укажите дату рождения'

      }
    },
    methods : {
      goTOChangeProfile(){
        this.$router.push('/profile/change')
      }
    },
    async mounted(){
      const user = await axios.get('/api/user/profile/me')
      console.log(user);
      if (user.data.User.birthday_date !==null) {//about
        this.birthday_date = user.User.data.birthday_date
      }
      if (user.data.User.about !==null) {//about
        this.description = user.User.data.about
      }
      if (user.data.User.phone_number !==null) {//phone
        this.phone = user.data.User.phone_number
      }
      if (user.data.User.city.city_name !==null) {//city
        this.city = user.data.User.city.city_name
      }
      if (user.data.User.fio !==null) {//fio
        this.fio = user.data.User.FIO
      }
      this.trainer = user.data.User.is_coach,
      this.email = user.data.User.email


      
    }
  }
  
  </script>
  
  <style scoped>
    .window-view-profile {
      background-color: #fff;
      border: 1px solid #efefef;
      width:70%;
      height:40%;
      position: absolute;
      left:0;
      right: 0;
      top:0;
      bottom:0;
      margin:auto;
      padding:1vw;
      display: flex;
      flex-direction: row;
      gap:1vw;
    }
  
    .profile-photo {
      width: 30%;
      height:100%;
      border: 1px solid #efefef;
      border-radius: 1vw;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      
    }
  
    .photo {
      width:300px;
      height:300px;
      background-color: #ddd;
      border-radius: 1vw;
      overflow: hidden;
    }
  
    .photo img {
      width:100%;
      height:100%;
    }
  
    .profile-content {
      width: 70%;
      height:76%;
      border-radius: 1vw;
      display:flex;
      flex-direction: column;
      padding: 2.5vw 0;
      overflow: hidden;
    }
  
    .content-line {
      width:100%;
      display:flex;
      justify-content: left;
      align-items: center;
      row-gap:10px;
    }
  
  #city{
      height:15%;
      flex-direction: row;
    }
  
  #username {
      height:60%;
      flex-direction: row;
    }
  
  #feedback {
      height: 20%;
      flex-direction: row;
    }
  
  #description {
      height:5%;
      flex-direction: row;
    }
  
  .tabs {
    display:flex;
    flex-direction: row;
    justify-content: left;
    align-items: center;
    padding: 0 2vw;
    width:100%;
    height:100%;
    gap:10px;
  }
  
  .tab {
    background-color: rgb(255, 145, 0);
    display:flex;
    text-align: center;
    font-size: 1.6vh;
    padding: 1.5vh 3vh;
    border-radius: .2vh;
    color:#fff;
    font-family: Arial, Helvetica, sans-serif;
    flex-direction: row;
    align-items: center;
    gap:10px;
    justify-content: center;
    font-weight: 600;
  }
  
  
  
  .text-username {
    height:100%;
    width:100%;
    display: flex;
    overflow:hidden;
    align-items: center;
    justify-content: left;
    padding-left:2vw;
    font-size: 5vh;
    font-family: Arial, Helvetica, sans-serif;
  }
  
  #feedback-tab {
    background-color: rgb(255, 145, 0);
    display:flex;
    text-align: center;
    font-size: 1.6vh;
    padding: 1vh 3vh;
    border-radius: .2vh;
    color:#fff;
    font-family: Arial, Helvetica, sans-serif;
    display:flex;
    flex-direction: row;
    align-items: center;
    gap:10px;
    justify-content: center;
    font-weight: 600;
    white-space: nowrap;
  }
  
  .text-tab {
    white-space: nowrap;
    text-overflow:ellipsis;
    overflow: hidden;
  }
  
  .tab img {
    width: 1.4vh;
    height:1.4vh;
    filter:invert(1);
  }
  
  #feedback-tab {
    background-color: rgb(59, 59, 59);
    color:#ddd;
    font-size: 1.3vh;
    font-weight: 600;
  }
  
  #decription {
    display:flex;
    flex-direction: row;
    width:100%;
    height:100%;
  }
  
  .left-content {
    width: 70%;
    height: 90%;
    display: flex;
    justify-content: center;
  }
  .right-content {
    width: 30%;
    height: 90%;
  }
  
  .text-description  {
    font-size: 2vh;
    width:88%;
    height:100%;
    overflow: hidden;
    text-align: justify;
    height:6vw;
  }
  
  #tabs-description {
    display: flex;
    flex-direction: column;
    gap:1vh;
    height: 100%;
    justify-content: top;
    padding: 0 2vh;
    
  }
  
  #description-tab {
    background-color: rgb(255, 153, 1);
  }
  
  #edit-tab {
    background-color: rgb(47, 47, 47);
    font-size: 1.3vh;
    padding: 2vh 3vh;
    height: 100%;
  }
  
  #edit-tab:hover {
    background-color: #6c6c6c;
    cursor:pointer;
    transition:all .4s ease;
  }
  
  #description-tab:hover {
    background-color: #d77700;
    cursor:pointer;
    transition:all .4s ease;
  }
  
  
  
  @media (max-width: 1650px) {
    .photo {
      width:270px;
      height:270px;
    }
    
    }
  
    @media (max-width: 1380px) {
      .window-view-profile {
        flex-direction: column;
        width:60vw;
        height:70vh;
      }
      .profile-photo {
      width: 100%; }
      .profile-content {
      width: 100%; }
      .photo {
        width:200px;
        height:200px;
      }
      .tabs {
        justify-content: center;
      }
      .text-username {
        justify-content: center;
      }
      #decription {
        flex-direction: column;
      }
      .left-content {
        width: 100%;
        height: 50%;
      }
      .right-content {
        width: 100%;
        height: 50%;
      }
      .text-description {
        font-size:1.5vh;
        height:4vw;
      }
      .left-content {
        height:30%;
      }
      .tab {
        height:1vh;
      }
      .window-view-profile {
      height:80%;
    }
    }
  
    @media (max-width: 900px) { 
      
      .photo {
        width:250px;
        height:250px;
      }
      #decription {
        flex-direction: column;
      }
      .left-content {
        width: 100%;
        height: 50%;
      }
      .right-content {
        width: 100%;
        height: 50%;
      }
      .text-username {
        font-size: 3.5vh;
        overflow: hidden;
      }
      .tab {
        font-size:1.2vh;
      }
      .text-description {
        font-size:1.2vh;
      }
      #feedback-tab {
        font-size:1vh;
        padding: 1vh 1vh;
      }
      .photo {
        width:180px;
        height:180px;
      }
      .tab {
        width:88%;
      }
    }
  
    @media (max-width: 600px) {
      .window-view-profile {
        flex-direction: column;
        width:70%;
        height:70vh;
      }
      #tabs-description {
        flex-direction: column;
      }
      #decription {
        flex-direction: column;
      }
      .left-content {
        width: 100%;
        height: 50%;
      }
      .right-content {
        width: 100%;
        height: 50%;
      }
      
    }
  
    @media (max-width: 450px) {
      .tab {
        width:83%;
      }
      .left-content {
        height:30%;
      }
      .window-view-profile {
        height:80%;
      }
      .profile-photo {
        height:30%;
      }
      .content-line {
        height:10%;
      }
      .text-username {
        height:50%;
      }
      #username {
        height:20%;
      }
      .text-description {
        height:100%;
        overflow: hidden;
      }
      .tab {
        border-radius: 10vw;
      }
      #feedback-tab {
        border-radius: 10vw;
      }
      #name-city {
        width:30%;
      }
      #name-status {
        width:30%;
      }
    }
  
  </style>