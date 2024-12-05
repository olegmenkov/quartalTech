// src/main.js
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

import axios from 'axios';

Vue.config.productionTip = false;

// Set up axios to include the access token in headers
axios.interceptors.request.use(
  config => {
    const token = store.state.token;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');