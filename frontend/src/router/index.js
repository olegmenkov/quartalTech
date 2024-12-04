import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/LoginPage.vue';
import Register from '../components/Register.vue';
import ApartmentList from '../components/ApartmentList.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/apartments', component: ApartmentList },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});