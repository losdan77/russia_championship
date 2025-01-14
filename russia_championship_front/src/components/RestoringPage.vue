<template>
    <div class="window-restoring-access">
        <div class="left-side">
            <div class="logo-line">
                <img src="../assets/yandex.png"/>
            </div>
            <div class="main-text-line">
                Восстановление<br> доступа
            </div>
            <div class="additional-text-line" v-if="!isAuthorized && !isCodeCorrect">
                Укажите адрес электронной почты<br>
                куда мы отправим одноразовый пароль
            </div>

            <div class="additional-text-line" v-if="isAuthorized && !isCodeCorrect">
                Введите проверочный код<br>
                отправленный на вашу почту
            </div>

            <div class="additional-text-line" v-if="isAuthorized && isCodeCorrect">
                Введите новый пароль<br>
                для завершения операции
            </div>
        </div>
        <!-- EMAIL -->
        <div class="right-side" v-if="!isAuthorized && !isCodeCorrect">
            <div class="empty-line"></div>
            <div class="input-line">
                <label for="email">Почтовый адрес</label>
                <input type="email" id="email" v-model="email"  required/>
            </div>
            <div class="btn-line">
                <div class="btn-sign-in" @click="Authorization">Далее</div>
            </div>
            <div class="empty-line"></div>
        </div>
        <!-- AUTHCODE -->
        <div class="right-side-2" v-if="isAuthorized && !isCodeCorrect">
            <div class="empty-line"></div>
            <div class="input-line">
                <label for="email">Код аутентификации</label>
                <input type="text" id="password" v-model="authCode" required />
            </div>
            <div class="btn-line">
                <div class="btn-sign-in" @click="goToNextPage">Далее</div>
            </div>
            <div class="empty-line"></div>
        </div>
        <!-- password -->
        <div class="right-side-2" v-if="isAuthorized && isCodeCorrect">
            <div class="empty-line"></div>
            <div class="input-line">
                <label for="email">Новый пароль</label>
                <input type="password" class="password" v-model="password" required />
            </div>
            <div class="input-line">
                <label for="email">Повторите новый пароль</label>
                <input type="password" class="password" v-model="verify_password" required />
            </div>
            <div class="btn-line">
                <div class="btn-sign-in" @click="SubmitRestoring">Восстановить</div>
            </div>
            <div class="empty-line"></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import eventBus from '../eventBus';
export default {
    data() {
        return {
            email: '',
            authCode: '',
            password: '',
            verify_password: '',
            isAuthorized: false,
            isCodeCorrect: false
        };
    },
    methods: {
        async Authorization() {
            try {
                const response = await axios.post(`/api/user/dont_remember_password?email=${this.email}`)
                if (response.status === 200) {
                    this.isAuthorized = true;
                }
            } catch (error) {
                eventBus.emit('show-modal', 'Пользователя с такой почтой в системе нет');
            }

        },
        async goToNextPage() {
            try {
                const response = await axios.post(`/api/user/verify_singlemode_code_from_mail?email=${this.email}&code=${this.authCode}`)
                if (response.status === 200) {
                    this.isCodeCorrect = true;
                }
            } catch (error) {
                eventBus.emit('show-modal', 'Неверный проверочный код ');
            }
            

        },
        async SubmitRestoring() {
            try {
                const response = await axios.post(`/api/user/create_new_password`,{
                    email: this.email,
                    new_password: this.password,
                    verify_new_password: this.verify_password
                },{timeout:2000})
            console.log(response)
            if (response.status === 200) {
                eventBus.emit('show-modal', `Доступ к аккаунту ${this.email} восстановлен`);
                this.$router.push('/auth');
                }
            } catch (error) {
                eventBus.emit('show-modal', 'Приносим извенения, повторите попытку позже');  
            }

            
        }
    }
}
</script>

<style scoped>
    .window-restoring-access {
        background-color: #ddd;
        width:50vw;
        height: 40vh;
        position: absolute;
        top:0;
        bottom:0;
        left:0;
        right:0;
        margin:auto;
        display:flex;
        flex-direction: row;
        -webkit-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
        -moz-box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
        box-shadow: 0px 0px 35px 6px rgba(34, 60, 80, 0.2);
    }

    .left-side {
        background-color: #f0f0f0;;
        height:100%;
        width:50%;
        display: flex;
        flex-direction: column;
    }

    .logo-line {
        height:35%;
        width:100%;
        display:flex;
        justify-content: left;
        align-items: center;
        padding-left:2vw;
    }

    .logo-line img {
        width:3vw;
        height:3vw;
        filter:invert(1);
    }

    .main-text-line {
        height:25%;
        width:100%;
        display:flex;
        justify-content: left;
        align-items: top;
        padding-left:2vw;
        font-size: 4vh;
        font-family: Arial, Helvetica, sans-serif;
    }

    .additional-text-line {
        height:40%;
        width:100%;
        display:flex;
        justify-content: left;
        align-items: top;
        padding-left:2vw;
        font-size: 2vh;
        font-family: Arial, Helvetica, sans-serif;
        padding-top: 1vw;
    }
    
    .right-side {
        background-color: #fff;
        height:100%;
        width:50%;
        display:flex;
        flex-direction: column;
    }

    .empty-line {
        height:30%;
        width:100%;
    }

    .input-line {
        height:25%;
        width:100%;
        display:flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }


    .wrapper-input:hover {
        transition: all .4s ease;
        border-bottom:1px solid #9d9d9d;
        cursor:pointer;
        }
    .input-line label {
        height:2vh;
        padding-left:2vh;
        padding-top:.5vh;
        font-size: 1.5vh;
        color:#919191;
        font-family: Arial, Helvetica, sans-serif;
        background-color: #f0f0f0;
        width:73.5%;
        }

    .input-line input {
        background-color: #f0f0f0;
        outline: 0;
        width:70%;
        border:0;
        height:4vh;
        padding-left:3.5vh;
        font-size: 1.8vh;
        font-family: Arial, Helvetica, sans-serif;
        cursor:pointer;
        }

    .btn-line {
        height:15%;
        width:100%;
        display:flex;
        flex-direction: column;
        align-items: center;
    }
    .btn-sign-in {
        display: flex;
        background-color: #333;
        font-size:2vh;
        align-items: center;
        justify-content: center;
        padding: .5vh 5vh;
        height:3vh;
        font-family: Arial, Helvetica, sans-serif;
        color:#fff;
        width:4vw;
        margin-left:10vw;
        }

    .btn-sign-in:hover {
        background-color: #bfbfbf;
        cursor:pointer;
        }
    
    .right-side-2 {
        background-color: #fff;
        height:100%;
        width:50%;
        display:flex;
        flex-direction: column;
    }

    @media (max-width:1380px) {
        .left-side {
            padding: 10px;
        }
        .right-side {
            padding: 10px;
        }
        .right-side-2 {
            padding: 10px;
        }
        .input-line label {
            width:80%;
            height:15%;
        }
        .input-line input {
            width:80%;
            padding:1vh;
            height:15%;
        }
        .btn-sign-in {
            margin-left:0;
        }
        .main-text-line {
            font-size: 23px;
        }
        .additional-text-line {
            font-size: 13px;
        }
    }
    @media (max-width:1000px) {
        .window-restoring-access {
            flex-direction: column;
            width:40%;
            height:90%;
        }
        .left-side {
            width:100%;
        }
        .right-side {
            width:100%;
        }
        .right-side-2 {
            width:100%;
        }
        .logo-line img {
            width:50px;
            height:50px;
        }
    }

    @media (max-width:500px) {
        .window-restoring-access {
            flex-direction: column;
            width:70%;
            height:90%;
        }
        .left-side {
            width:100%;
        }
        .right-side {
            width:100%;
        }
        .right-side-2 {
            width:100%;
        }
        .logo-line {
            justify-content: center;
        }
        .logo-line img {
            width:50px;
            height:50px;
        }
        .main-text-line {
            font-size: 21px;
            text-align: center;
            justify-content: center;
        }
        .additional-text-line {
            font-size: 12px;
            text-align: center;
            justify-content: center;
        }
    }
</style>
