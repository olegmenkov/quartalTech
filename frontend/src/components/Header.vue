<!-- src/components/Header.vue -->
<template>
  <header>
    <nav>
      <div class="logo">
        <router-link to="/">RealEstatePortal</router-link>
      </div>
      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/predict" v-if="isLoggedIn">Predict Price</router-link>
      </div>
      <div class="auth">
        <button v-if="!isLoggedIn" @click="goToLogin">Login</button>
        <div v-else class="user-menu">
          <img :src="userAvatar" @click="toggleMenu" class="avatar"/>
          <div v-if="showMenu" class="menu">
            <router-link to="/profile">Profile</router-link>
            <button @click="logout">Logout</button>
          </div>
        </div>
        <button v-if="isLoggedIn" @click="goToCreateListing">Create Listing</button>
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
      // Return the user's avatar image URL or a default image
      return userImage
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
    }
  }
};
</script>

<style scoped>
/* Add styles for header */
</style>