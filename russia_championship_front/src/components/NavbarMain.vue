<template>
  <nav class="navbar">
    <div class="navbar-logo" @click="goToMain">
      <img src="..//assets/logo.png" alt="Logo" class="logo" @click="goToMain"/>
    </div>

    <div class="navbar-buttons desktop-buttons">
      <button class="navbar-button" id="btn-telegram-2">
        <img src="..//assets/telegram.png"/>
      </button>
      <button class="navbar-button" id="btn-telegram"><div class="img"></div></button>
      <button class="navbar-button" id="btn-input" @click="goToProfile" v-if="onProfile">Профиль</button>
      <button class="navbar-button" @click="logout" id="btn-reg">
        <div class="text-btn" @click="logout">Выйти</div> <img src="..//assets/btn-exit.png"/>
        </button>
      
    </div>

    <div class="mobile-menu-icon" @click="toggleMenu">
      <span :class="{ 'open': isMenuOpen }"></span>
      <span :class="{ 'open': isMenuOpen }"></span>
      <span :class="{ 'open': isMenuOpen }"></span>
    </div>

    <div v-if="isMenuOpen" class="mobile-menu">
      <button class="navbar-button" id="btn-menu" @click="goToProfile">Профиль</button>
      <button class="navbar-button" id="btn-menu" @click="logout">Выйти</button>
      <button class="navbar-button" id="btn-menu-telegram" @click="closeMenu">Телеграм</button>
    </div>
  </nav>
</template>

<script>
import axios from 'axios';
import eventBus from '../eventBus';

export default {
  data() {
    return {
      isMenuOpen: false,
      onProfile : false
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
    GoToReg(){
      this.isMenuOpen = false;
      this.$router.push('/reg')
    },  
    Authorization(){
      this.isMenuOpen = false;
      this.$router.push('/auth')
    },
    goToProfile(){
      // const url =  this.$route.fullPath
      
      // if (url === '/profile') {
      //   eventBus.emit('show-modal', 'Вы в своём профиле');
      // }
      this.$router.push('/profile')
    },
    async logout(){
      this.$router.push('/')
      const response = await axios.post('/api/user/logout')
      eventBus.emit('show-modal', 'Вы вышли из аккаунта');
      this.$emit('LogoutNav')
    },
    goToMain(){
      this.$router.push('/')
    }
  },
  mounted(){
    if (this.$route.fullPath === '/profile') {
      this.onProfile = false
    }else {
      this.onProfile = true
    }

  }
};
</script>

<style scoped>

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width:100%;
  background-color: #ffffff;
  color: white;
  -webkit-box-shadow: 0px 10px 8px -4px rgba(34, 60, 80, 0.48);
-moz-box-shadow: 0px 10px 8px -4px rgba(34, 60, 80, 0.48);
box-shadow: 0px 10px 8px -4px rgba(34, 60, 80, 0.48);
}


.navbar-logo .logo {
  width: 40px;
  filter: invert(.7);
  cursor: pointer;
  margin-left:7vw;
}


.desktop-buttons {
  display: flex;
  flex-direction: row;
  align-items: center;
  height:6vh;
  margin-right:7vw;
}

.navbar-button {
  background: none;
  border: none;
  font-size: 1.5vh;
  cursor: pointer;
  padding: 0 2vw;
  height:6vh;
  font-family:Golos-Text;
  transition: all .4s ease;
}

#btn-input {
  background-color: rgb(49,68,104);
  color:#ffffff;
  font-weight: 600;
}

#btn-input:hover {
  background-color: rgb(37, 51, 77);
}

#btn-reg {
  background-color: #fff;
  color:#323232;
  font-weight: 600;
  column-gap:10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

#btn-reg img {
  width:15px;
  height:15px;
  filter:invert(.2)
}

#btn-reg:hover {
  background-color: #f4f4f4;
  color:rgb(83, 114, 171);
}

#btn-telegram {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
}

#btn-telegram:hover {
  background-color: #f4f4f4;
  
}

#btn-telegram .img {
  width:2.5vh;
  height:2.5vh;
  background-image: url("../assets/telegram-black.png");
  background-size: cover;
  transition: all .4s ease;
}

#btn-telegram:hover .img {
  background-image: url("../assets/telegram-blue.png");
}

.mobile-menu-icon {
  display: none;
  flex-direction: column;
  cursor: pointer;
  
}

.mobile-menu-icon span {
  background-color: rgb(28, 28, 28);
  height: 2px;
  margin: 4px 0;
  width: 25px;
  transition: 0.3s;
  
}

.open:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.open:nth-child(2) {
  opacity: 0;
}

.open:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

/* Стили для мобильного меню */
.mobile-menu {
  display: flex;
  flex-direction: column;
  gap: 10px;
  background-color: #ffffff00;
  padding: 10px;
}

#btn-telegram-2 {
  background-color: #2AABEE;
  padding: 0 .7vh;
  border-radius: 50%;
  display: none;
  height:3vh;
  width:3vh;
}

#btn-telegram-2 img {
  width:15px;
  height:15px;
  
}

#btn-telegram img {
  width:2.3vh;
  height:2.3vh;
  filter:invert(0.8)
}

#btn-menu {
  color:#101010;
  background-color: #ededed;
  padding:1vh 3vw;
  font-family:Verdana, Geneva, Tahoma, sans-serif;
}

#btn-menu-telegram {
  color:#ffffff;
  background-color: #1a9ed6;
  padding:1vh 1vw;
  border-radius: 0;
  font-family:Verdana, Geneva, Tahoma, sans-serif;
}


@media (max-width: 1000px) {
  .navbar-button {
    font-size: 1.3vh;
  }
  #btn-telegram-2 {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #btn-telegram {
    display: none;
  }
  .navbar-logo .logo {
  width: 30px;
}
.desktop-buttons { 
  gap:1vh;
}
}

@media (max-width: 768px) {
  .desktop-buttons {
    display: none;
  }
  
  .mobile-menu-icon {
    display: flex;
  }
  .navbar{
    padding-top:1vw;
    padding-bottom:1vw;
  }
  .navbar {
    display:flex;
    flex-direction: row;
  }
}

@media (max-width: 580px) {
  .navbar {
    display:flex;
    flex-direction: row;
    width:120%;
  }
}
@media (max-width: 450px) {
  .navbar {
    display:flex;
    flex-direction: row;
    width:140%;
  }
}
</style>