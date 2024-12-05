// src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import CreateListing from '../views/CreateListing.vue';
import Profile from '../views/Profile.vue';
import Predict from '../views/Predict.vue';
import NotFound from '../views/NotFound.vue';

import store from '../store';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/login', name: 'Login', component: Login },
    { path: '/register', name: 'Register', component: Register },
    {
      path: '/create-listing',
      name: 'CreateListing',
      component: CreateListing,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      meta: { requiresAuth: true }
    },
    {
      path: '/predict',
      name: 'Predict',
      component: Predict,
      meta: { requiresAuth: true }
    },
    { path: '*', name: 'NotFound', component: NotFound }
  ]
});

// Navigation Guards
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = store.state.token;

  if (requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;