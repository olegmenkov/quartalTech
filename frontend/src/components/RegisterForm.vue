<!-- src/components/RegisterForm.vue -->
<template>
  <div class="register-page">
    <div class="register-form">
      <h2>Регистрация</h2>
      <form @submit.prevent="registerUser">
        <div class="form-group">
          <label for="username">Логин:</label>
          <input id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input id="password" v-model="password" type="password" required />
        </div>
        <div class="form-group">
          <label for="password2">Повторите пароль:</label>
          <input id="password2" v-model="password2" type="password" required />
        </div>
        <div class="form-group">
          <label for="admin_key">Секретный ключ администратора:</label>
          <input id="admin_key" v-model="admin_key" type="password" />
        </div>
        <button type="submit" class="btn">Зарегистрироваться</button>
      </form>
      <p class="login-link">
        Уже есть аккаунт? <router-link to="/login">Войти</router-link>
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
          // Регистрация прошла успешно, перенаправление на страницу входа
          alert('Регистрация прошла успешно');
          this.$router.push('/login');
        })
        .catch(error => {
          console.error(error);
          // Обработка ошибки, отображение сообщения
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
/* Стили для страницы регистрации */
.register-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px); /* Вычитание высоты хедера */
  background-color: #ecf0f1;
}

.register-form {
  background-color: #ffffff;
  padding: 40px 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.register-form h2 {
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

.login-link {
  text-align: center;
  margin-top: 20px;
  color: #34495e;
}

.login-link a {
  color: #1abc9c;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
