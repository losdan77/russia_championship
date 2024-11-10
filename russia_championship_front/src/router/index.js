import { createRouter, createWebHistory } from 'vue-router';
import PrimaryPage from '../components/PrimaryPage.vue';
import RegisterPage from '../components/RegisterPage.vue'; 
import LoginPage from '../components/LoginPage.vue';       
import ProfilePage from '../components/ProfilePage.vue';
import RedactPage from '../components/RedactPage.vue';
import MainPage from '../components/MainPage.vue';
import RestoringPage from '../components/RestoringPage.vue';
import ChangePassword from '../components/ChangePassword.vue';

import axios from 'axios';

const routes = [
  { path: '/', component: PrimaryPage },
  { path: '/reg', component: RegisterPage },
  { path: '/auth', component: LoginPage },
  { path: '/profile', component: ProfilePage },
  { path: '/profile/change', component: RedactPage},
  { path: '/info', component: MainPage},
  { path: '/user/restoring', component: RestoringPage},
  { path: '/user/changepass', component: ChangePassword},

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
