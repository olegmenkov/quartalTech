<!-- src/components/RegisterForm.vue -->
<template>
  <div class="register-form">
    <h2>Регистрация</h2>
    <form @submit.prevent="registerUser">
      <label>Логин:</label>
      <input v-model="username" required />

      <label>Пароль:</label>
      <input v-model="password" type="password" required />

      <label>Повторите пароль:</label>
      <input v-model="password2" type="password" required />

      <label>Секретный ключ администратора:</label>
      <input v-model="admin_key" type="password" />

      <button type="submit">Зарегистрироваться</button>
    </form>
    <p>
      <router-link to="/login">Уже есть аккаунт? Войти</router-link>
    </p>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
      password2: '',
      admin_key: ''
    };
  },
  methods: {
    ...mapActions(['register']),
    registerUser() {
      if (this.password !== this.password2) {
        alert('Пароли не совпадают');
        return;
      }

      const userData = {
        username: this.username,
        password: this.password,
        admin_key: this.admin_key || null
      };

      this.register(userData)
        .then(() => {
          // Registration successful, redirect to login
          alert('Регистрация прошла успешно');
          this.$router.push('/login');
        })
        .catch(error => {
          console.error(error);
          // Handle error, show message
          if (error.response && error.response.data.detail) {
            alert(`Ошибка регистрации: ${error.response.data.detail}`);
          } else {
            alert('Ошибка регистрации');
          }
        });
    }
  }
};
</script>

<style scoped>
/* Add styles for the registration form */
.register-form {
  max-width: 400px;
  margin: 0 auto;
}
.register-form label {
  display: block;
  margin-top: 10px;
}
.register-form input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
.register-form button {
  margin-top: 20px;
  width: 100%;
  padding: 10px;
}
</style>
