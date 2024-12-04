<template>
  <div class="login-container animate__animated animate__fadeIn">
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Имя пользователя" required />
      <input type="password" v-model="password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://app:8000/users/login', {
          username: this.username,
          password: this.password,
        });
        localStorage.setItem('token', response.data.access_token);
        this.$router.push('/apartments');
      } catch (err) {
        this.error = 'Неправильные данные для входа';
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.error {
  color: red;
}
</style>
