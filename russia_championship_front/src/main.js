import { createApp } from 'vue';
import App from './App.vue';
import router from './router';  // Подключаем маршрутизатор
import vue3GoogleLogin from 'vue3-google-login';

const app = createApp(App);
app.use(router);  // Используем маршрутизатор

// app.use(vue3GoogleLogin, {
//     clientId: '73730114414-4hmh3j7il9rg3na6p9qmp4bo983ijb23.apps.googleusercontent.com ',
// });
app.mount('#app');
