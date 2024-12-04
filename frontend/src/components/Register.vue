<template>
  <div class="register-container animate__animated animate__fadeIn">
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="Имя пользователя" required />
      <input type="password" v-model="password" placeholder="Пароль" required />
      <input type="password" v-model="confirmPassword" placeholder="Повторите пароль" required />
      <input
        type="text"
        v-model="adminKey"
        placeholder="Админ ключ (опционально для администраторов)"
      />
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="success" class="success">{{ success }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "RegisterPage", // Используем многословное имя
  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
      adminKey: "",
      error: null,
      success: null,
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        this.error = "Пароли не совпадают.";
        return;
      }
      try {
        await axios.post("https://app:8000/users/", {
          username: this.username,
          password: this.password,
          admin_key: this.adminKey,
        });
        this.success = "Регистрация успешна! Теперь вы можете войти.";
        this.error = null;
      } catch (err) {
        this.error = err.response?.data?.detail || "Ошибка регистрации.";
        this.success = null;
      }
    },
  },
};
</script>

<style scoped>
.register-container {
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
.success {
  color: green;
}
</style>
