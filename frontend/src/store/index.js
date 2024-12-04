import { createStore } from "vuex";
import axios from "axios";

export const store = createStore({
  state: {
    user: null,
    token: localStorage.getItem("token") || null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
    },
    clearAuth(state) {
      state.user = null;
      state.token = null;
      localStorage.removeItem("token");
    },
  },
  actions: {
    async login({ commit }, { username, password }) {
      try {
        const response = await axios.post("http://localhost:8000/users/login", {
          username,
          password,
        });
        commit("setToken", response.data.access_token);
        commit("setUser", { id: response.data.id, username });
        return response.data;
      } catch (err) {
        throw err.response?.data?.detail || "Ошибка при авторизации.";
      }
    },
    async fetchUser({ commit, state }) {
      try {
        if (!state.token) return;
        const response = await axios.get("http://localhost:8000/users/", {
          headers: { Authorization: `Bearer ${state.token}` },
        });
        commit("setUser", response.data);
      } catch (err) {
        commit("clearAuth");
      }
    },
    logout({ commit }) {
      commit("clearAuth");
    },
  },
  getters: {
    isAuthenticated(state) {
      return !!state.token;
    },
    getUser(state) {
      return state.user;
    },
  },
});
