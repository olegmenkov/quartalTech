<!-- src/components/LoginForm.vue -->
<template>
  <div class="login-page">
    <div class="login-form">
      <h2>Вход в аккаунт</h2>
      <form @submit.prevent="loginUser">
        <div class="form-group">
          <label for="username">Логин:</label>
          <input id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input id="password" v-model="password" type="password" required />
        </div>
        <button type="submit" class="btn">Войти</button>
      </form>
      <p class="register-link">
        Нет аккаунта? <router-link to="/register">Зарегистрируйтесь</router-link>
      </p>
    </div>
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
        .then(() => {
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
          // Обработка ошибок и отображение сообщения
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
/* Стили для страницы входа */
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px); /* Вычитание высоты хедера */
  background-color: #ecf0f1;
}

.login-form {
  background-color: #ffffff;
  padding: 40px 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-form h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  color: #34495e;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

.form-group input:focus {
  border-color: #1abc9c;
  outline: none;
}

.btn {
  width: 100%;
  padding: 12px;
  background-color: #1abc9c;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
}

.btn:hover {
  background-color: #16a085;
}

.register-link {
  text-align: center;
  margin-top: 20px;
  color: #34495e;
}

.register-link a {
  color: #1abc9c;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>
