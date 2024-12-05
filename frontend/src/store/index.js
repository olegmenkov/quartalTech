// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const backendUrl = process.env.VUE_APP_BACKEND_URL || 'http://localhost:8000';

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',
    user: null,
    apartments: [],
    filters: {},
    isAdmin: false
  },
  mutations: {
    AUTH_SUCCESS(state, { token, user }) {
      state.token = token;
      state.user = user;
      state.isAdmin = user.role === 'admin';
    },
    AUTH_LOGOUT(state) {
      state.token = '';
      state.user = null;
      state.isAdmin = false;
    },
    SET_APARTMENTS(state, apartments) {
      state.apartments = apartments;
    },
    SET_FILTERS(state, filters) {
      state.filters = filters;
    }
  },
  actions: {
    login({ commit }, userData) {
      return axios.post(`${backendUrl}/users/login`, userData)
        .then(response => {
          console.log(response)
          const token = response.data.access_token;
          const userId = response.data.id;

          localStorage.setItem('token', token);
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

          return axios.get(`${backendUrl}/users/`, { headers: { Authorization: `Bearer ${token}` } })
            .then(res => {
              const user = res.data;
              commit('AUTH_SUCCESS', { token, user });
            });
        });
    },
    register({ commit }, userData) {
      return axios.post(`${backendUrl}/users/`, userData)
        .then(() => {
          // Registration successful, redirect to login
        });
    },
    logout({ commit }) {
      commit('AUTH_LOGOUT');
      localStorage.removeItem('token');
      delete axios.defaults.headers.common['Authorization'];
    },
    fetchApartments({ commit }, filters = {}) {
      let params = new URLSearchParams(filters).toString();
      return axios.get(`${backendUrl}/apartments/?${params}`)
        .then(response => {
          commit('SET_APARTMENTS', response.data);
        });
    },
    createApartment({ dispatch }, apartmentData) {
      return axios.post(`${backendUrl}/apartments/`, apartmentData)
        .then(() => {
          dispatch('fetchApartments');
        });
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    isAdmin: state => state.isAdmin,
    apartments: state => state.apartments,
    filters: state => state.filters
  }
});