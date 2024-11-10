<template>

  <div class="window">
    <section class="left-section">
      <div class="section" id="section-1">
        <div class="content-section-1">
          <div class="logo-img">
              <div class="profile-picture">
                <img :src="image_url" class="main-image" v-if="image_url">
              </div>
          </div>
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
            Физическое лицо
          </div>
          <div 
            :class="['selector-option2', { 'active': userType === 'organization' }]" 
            @click="setUserType('organization')"
          >
            Юридическое лицо
          </div>
        </div>
        </div>
        <div class="input-wrapper">
          <div class="wrapper-input">
          <label for="fullName">ФИО*</label>
          <input type="text" id="fullName" v-model="fullName" required />
        </div>
        <div class="line-wrapper">
        <div class="wrapper-input">
          <label for="email">Почта*</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-row">
          <div class="wrapper-input" id="nubmer-phone">
            <label for="phone">Номер телефона*</label>
            <input type="tel" id="phone" v-model="phone" required />
          </div>
          <div class="wrapper-input" id="city-user">
            <label for="city">Город</label>
            <input type="text" id="city" v-model="city" />
          </div>
        </div>
        <div class="form-row" v-if="userType=='organization'">
          <div class="wrapper-input" id="type-org">
            <label>Тип организации</label>
            <div class="dropdown">
                <select v-model="organizationType">
                    <option disabled value="">Выберите тип организации</option>
                    <option value="ИП">Индивидуальный предприниматель</option>
                    <option value="ООО">Общество с ограниченной ответственностью</option>
                    <option value="АО">Акционерное общество</option>
                    <option value="НКО">Некоммерческая организация</option>
                </select>
            </div>
          </div>
          <div class="wrapper-input" id="gos-num">
            <label for="govNumber">Государственный номер</label>
            <input type="text" id="govNumber" v-model="govNumber" />
          </div>
        </div>
  
        <div class="wrapper-input">
          <label for="password">Пароль*</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="wrapper-input">
          <label for="confirm-password">Подтвердите пароль*</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
        </div>
        <div class="wrapper-input" id="photo-wrapper">
        <div class="image-redactor">
              <input type="file" id="fileupload" name="image" @change="handleFileUpload" v-if="!image">
              <button v-if="image" @click="AddPhoto" class="save-button">Добавить</button>
            </div>
          </div>
        <div type="submit" class="register-button" @click="Register()">Зарегистрироваться</div>
        <p @click="GoToLogin()" class="GoToLogin">У меня уже есть аккаунт</p>
        <div class="logo-pic">
          <img src="../assets/yandex.png"/>
        </div>
        </div>
      </div>
      </div>
    </section>

  </div>
    
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        userType: 'individual',
        fullName: '',
        email: '',
        phone: '',
        city: '',
        organizationType: '',
        govNumber: '',
        password: '',
        confirmPassword: '',
        image: null,
        image_url: null,
      };
    },
    methods: {
      setUserType(type) {
        this.userType = type;
      },
      GoToLogin(){
        this.$router.push('/auth')
      },
      async Register(){
        //axios запрос для получения формы id пользователя
        const response = await axios.post('/api/user/registr', {
          email: this.email,
          password: this.password,
          password_verify: this.confirmPassword
        });
        console.log(response);
        if (!response.data) {
          return 0
        }
        alert('Успешно')
        this.$router.push('/profile')
      },
      handleFileUpload(event) {
        this.image = event.target.files[0];
        if (this.image) {
          this.image_url = URL.createObjectURL(this.image); // Предпросмотр изображения
        }
      },
      submitForm() {
        if (this.password !== this.confirmPassword) {
          alert("Пароли не совпадают");
        } else {
        }
      },
      async AddPhoto(){
        try {
          const id = this.$route.params.id
          const formData = new FormData();
          formData.append('file', this.image);
          console.log(this.image);
          const response = await axios.post(`/api/images/add_profile_image_to_s3?id_profile=${id}`, formData, {
            headers: {
              // 'Content-Type': 'multipart/form-data'
            }
        });
        const image_url = await axios.get(`/api/imagesget_url_image_profile_from_s3?id_profile=${id}`)
        this.image_url = image_url.data
        console.log(image_url.data);
        

        } catch (error) {
          console.log(error);
          
        }
        alert("Добавить фото")
      }
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
  font-family: Arial, Helvetica, sans-serif;
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
  font-family: Arial, Helvetica, sans-serif;
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
  font-family: Arial, Helvetica, sans-serif;
  cursor:pointer;
}

.input-wrapper select {
  background-color: #f0f0f0;
  outline: 0;
  border:0;
  height:2.5vh;
  padding-left:3.5vh;
  font-size: 1.5vh;
  font-family: Arial, Helvetica, sans-serif;
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
    
    font-family: Arial, Helvetica, sans-serif;
    color:#9d9d9d
  }
  .selector-option1 {
    flex: 1;
    text-align: center;
    padding: 10px;
    cursor: pointer;
    transition: background-color .6s ease;
    font-family: Arial, Helvetica, sans-serif;
    color:#9d9d9d
  }
  
  .selector-option1.active {
    background-color: #333;
    color: #fff;
    border-color: #333;
    font-weight: bold;
  }
  
  .selector-option1:not(.active):hover {
    background-color: #eee;
    
  }
  .selector-option2.active {
    background-color: #333;
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
  background-color: #333;
  font-size:2vh;
  align-items: center;
  justify-content: center;
  padding: .5vh 5vh;
  height:4vh;
  border-radius: 3vh;
  font-family: Arial, Helvetica, sans-serif;
  color:#fff;
  transition: all .4s ease;
  margin-top:1vw;
}

.register-button:hover {
  background-color: #bfbfbf;
  cursor:pointer;
}

p {
  font-family: Arial, Helvetica, sans-serif;
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
  border-radius: 1vh;
  padding:.5vh 2vh;
  cursor:pointer;
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
    width:80%;
  
  }
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

  </style>
  