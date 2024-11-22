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
              <div class="text-tab">Санкт-Петербург</div>
            </div>
  
            <div class="tab" id="name-status">
              <div class="text-tab">Физ.лицо</div>
            </div>
  
          </div>
        </div>
        <div class="content-line" id="username">
          <div class="text-username">Иванов Иван</div>
        </div>
        <div class="content-line" id="feedback">
          <div class="tabs">
            <div class="tab" id="feedback-tab">
              <img src="..//assets/phone.png">
              <div class="text-tab">7-(953)-291-76-79</div>
            </div>
            <div class="tab" id="feedback-tab">
              <img src="..//assets/mail.png">
              <div class="text-tab">zavatsk222222222iy_13@mail.ru</div>
            </div>
          </div>
        </div>
        <div class="content-line" id="decription">
          <div class="left-content">
            <div class="text-description">
              Я черный парнишка, в трусах еловая шишка: большая прибольшая. Кто сказал что я черный, я просто шоколадный. Бубылда яичная. Предоставляю свои услуги для дам 65+. 
              
            </div>
          </div>
          <div class="right-content">
            <div id="tabs-description">
            <div class="tab" id="description-tab">
              <div class="text-tab">Отзывы</div>
            </div>
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

  export default {
    data(){
      return {
        trainer : false,
        fio : '',
        Email : '',
        description : '',
        phone : '',
        city : ''

      }
    },
    methods : {
      goTOChangeProfile(){
        this.$router.push('/profile/change')
      }
    },
    async mounted(){
      const user = await axios.get('/api/user/profile/me')
      this.trainer = user.trainer,
      this.description = user.description,
      this.Email = user.email,
      this.phone = user.phone
      this.city = user.city,
      this.fio = user.fio
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