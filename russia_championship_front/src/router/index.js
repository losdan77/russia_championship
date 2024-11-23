import { createRouter, createWebHistory } from 'vue-router';
import PrimaryPage from '../components/PrimaryPage.vue';
import RegisterPage from '../components/RegisterPage.vue'; 
import LoginPage from '../components/LoginPage.vue';       
import ProfilePage from '../components/ProfilePage.vue';
import RedactPage from '../components/RedactPage.vue';
import MainPage from '../components/MainPage.vue';
import RestoringPage from '../components/RestoringPage.vue';
import ChangePassword from '../components/ChangePassword.vue';
import ModalCard from '../components/ModalCard.vue';
import CardPrimary from '../components/CardPrimary.vue';

const routes = [
  { path: '/', component: PrimaryPage },
  { path: '/reg', component: RegisterPage },
  { path: '/auth', component: LoginPage },
  { path: '/profile', component: ProfilePage },
  { path: '/profile/change', component: RedactPage},
  { path: '/info', component: MainPage},
  { path: '/info/card', component: ModalCard},
  { path: '/user/restoring', component: RestoringPage},
  { path: '/user/changepass', component: ChangePassword},
  { path: '/card', component: CardPrimary},

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
