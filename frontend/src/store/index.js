// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const backendUrl =
  process.env.VUE_APP_BACKEND_URL || 'https://direct-lionfish-vaguely.ngrok-free.app';

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',
    user: null,
    apartments: [],
    filters: {},
    isAdmin: false,
    fio: '',
    phone: '',
    email: '',
    price: null, // Добавлено: переменная для хранения предсказанной стоимости
  },
  mutations: {
    AUTH_SUCCESS(state, { token, user }) {
      state.token = token;
      state.user = user;
      state.isAdmin = user.role === 'admin';
      state.fio = user.fio;
      state.phone = user.phone;
      state.email = user.email;
    },
    AUTH_LOGOUT(state) {
      state.token = '';
      state.user = null;
      state.isAdmin = false;
      state.fio = '';
      state.phone = '';
      state.email = '';
    },
    SET_APARTMENTS(state, apartments) {
      state.apartments = apartments;
    },
    SET_FILTERS(state, filters) {
      state.filters = filters;
    },
    SET_PREDICTED_PRICE(state, price) {
      // Добавлено: мутация для обновления предсказанной стоимости
      state.price = price;
    },
  },
  actions: {
    login({ commit }, userData) {
      return axios
        .post(`${backendUrl}/users/login`, userData)
        .then((response) => {
          const token = response.data.access_token;
          const userId = response.data.id;

          localStorage.setItem('token', token);
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

          return axios
            .get(`${backendUrl}/users/`, {
              headers: { Authorization: `Bearer ${token}` },
            })
            .then((res) => {
              const user = res.data;
              commit('AUTH_SUCCESS', { token, user });
            });
        });
    },
    register({ commit }, userData) {
      return axios.post(`${backendUrl}/users/`, userData).then(() => {
        // Registration successful, redirect to login
      });
    },
    logout({ commit }) {
      commit('AUTH_LOGOUT');
      localStorage.removeItem('token');
      delete axios.defaults.headers.common['Authorization'];
    },
    fetchApartments({ commit }, filters = {}) {
      // Remove null or empty string values from filters
      const filteredFilters = Object.fromEntries(
        Object.entries(filters).filter(
          ([key, value]) => value !== null && value !== ''
        )
      );

      let params = new URLSearchParams(filteredFilters).toString();
      return axios
        .get(`${backendUrl}/apartments/?${params}`)
        .then((response) => {
          commit('SET_APARTMENTS', response.data);
        })
        .catch((error) => {
          console.error('Ошибка при загрузке квартир:', error);
        });
    },
    createApartment({ dispatch }, apartmentData) {
      return axios
        .post(`${backendUrl}/apartments/`, apartmentData)
        .then(() => {
          dispatch('fetchApartments');
        });
    },
    changeUserData({ commit }, { user_id, userData }) {
      console.log(user_id);
      console.log(userData);
      return axios.put(`${backendUrl}/users/${user_id}`, userData).then(() => {
        // Registration successful, redirect to login
      });
    },
    predictPrice({ commit }, params) {
      return axios
        .get(`${backendUrl}/calculate/`, { params })
        .then((response) => {
          commit('SET_PREDICTED_PRICE', response.data.price);
        })
        .catch((error) => {
          console.error('Ошибка при расчете стоимости:', error);
          throw error; // Rethrow the error to handle it in the component
        });
    },
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    isAdmin: (state) => state.isAdmin,
    apartments: (state) => state.apartments,
    filters: (state) => state.filters,
    price: (state) => state.price, // Добавлено: геттер для доступа к предсказанной стоимости
  },
});
