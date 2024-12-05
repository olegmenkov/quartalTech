<!-- src/components/LoginForm.vue -->
<template>
  <div class="login-form">
    <h2>Вход</h2>
    <form @submit.prevent="loginUser">
      <label>Логин:</label>
      <input v-model="username" required />

      <label>Пароль:</label>
      <input v-model="password" type="password" required />

      <button type="submit">Войти</button>
    </form>
    <p>
      <router-link to="/register">Нет аккаунта? Зарегистрируйтесь</router-link>
    </p>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    ...mapActions(['login']),
    loginUser() {
      const userData = {
        username: this.username,
        password: this.password
      };

      this.login(userData)
        .then(response => {
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
          // Handle error, show message
          if (error.response && error.response.data.detail) {
            alert(`Ошибка входа: ${error.response.data.detail}`);
          } else {
            alert('Ошибка входа');
          }
        });
    }
  }
};
</script>

<style scoped>
/* Add styles for the login form */
.login-form {
  max-width: 400px;
  margin: 0 auto;
}
.login-form label {
  display: block;
  margin-top: 10px;
}
.login-form input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
.login-form button {
  margin-top: 20px;
  width: 100%;
  padding: 10px;
}
</style>
