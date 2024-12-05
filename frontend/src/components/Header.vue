<!-- src/components/Header.vue -->
<template>
  <header class="header">
    <nav class="navbar">
      <div class="logo">
        <router-link to="/">КварталТек</router-link>
      </div>
      <div class="nav-links">
        <router-link to="/">Главная</router-link>
        <router-link to="/predict" v-if="isLoggedIn">Рассчитать стоимость</router-link>
      </div>
      <div class="auth">
        <button class="btn" v-if="!isLoggedIn" @click="goToLogin">Войти</button>
        <div v-else class="user-menu">
          <img :src="userAvatar" @click="toggleMenu" class="avatar"/>
          <div v-if="showMenu" class="menu">
            <router-link to="/profile">Профиль</router-link>
            <button class="btn-logout" @click="logoutUser">Выйти</button>
          </div>
        </div>
        <button class="btn" v-if="isLoggedIn" @click="goToCreateListing">Создать объявление</button>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapState, mapActions } from 'vuex';

import userImage from '@/assets/user.png';

export default {
  data() {
    return {
      showMenu: false
    };
  },
  computed: {
    ...mapState(['user']),
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userAvatar() {
      // Возвращает аватар пользователя или изображение по умолчанию
      return userImage;
    }
  },
  methods: {
    ...mapActions(['logout']),
    goToLogin() {
      this.$router.push('/login');
    },
    goToCreateListing() {
      this.$router.push('/create-listing');
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    logoutUser() {
      this.logout();
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
/* Стили для хедера */
.header {
  background-color: #2c3e50;
  padding: 10px 20px;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo a {
  color: #ecf0f1;
  font-size: 24px;
  font-weight: bold;
  text-decoration: none;
}

.nav-links {
  display: flex;
  align-items: center;
}

.nav-links a {
  color: #ecf0f1;
  margin-right: 15px;
  text-decoration: none;
  font-size: 18px;
}

.nav-links a:hover {
  color: #1abc9c;
}

.auth {
  display: flex;
  align-items: center;
}

.btn {
  background-color: #1abc9c;
  color: #fff;
  border: none;
  padding: 8px 15px;
  margin-left: 10px;
  cursor: pointer;
  border-radius: 4px;
}

.btn:hover {
  background-color: #16a085;
}

.user-menu {
  position: relative;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
}

.menu {
  position: absolute;
  top: 50px;
  right: 0;
  background-color: #34495e;
  border-radius: 4px;
  overflow: hidden;
  z-index: 1000;
}

.menu a,
.menu button {
  display: block;
  padding: 10px 15px;
  color: #ecf0f1;
  text-decoration: none;
  white-space: nowrap;
}

.menu a:hover,
.menu button:hover {
  background-color: #1abc9c;
}

.btn-logout {
  background: none;
  border: none;
  color: #ecf0f1;
  width: 100%;
  text-align: left;
  padding: 10px 15px;
  cursor: pointer;
}

.btn-logout:hover {
  background-color: #e74c3c;
}
</style>
