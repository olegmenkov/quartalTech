<!-- src/components/Profile.vue -->
<template>
  <div class="profile-page">
    <div class="profile-form">
      <h2>Профиль</h2>
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label>Логин:</label>
          <input v-model="form.username" required disabled />
        </div>

        <div class="form-group">
          <label>Пароль:</label>
          <input v-model="form.password" type="password" />
        </div>

        <div class="form-group">
          <label>Повторите пароль:</label>
          <input v-model="form.password2" type="password" />
        </div>

        <button type="submit" class="btn">Обновить профиль</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  data() {
    return {
      form: {
        username: '',
        password: '',
        password2: ''
      }
    };
  },
  computed: {
    ...mapState(['user']),
  },
  created() {
    this.form.username = this.user.username;
  },
  methods: {
     ...mapActions(['changeUserData']),
    updateProfile() {
      if (this.form.password !== this.form.password2) {
        alert('Пароли не совпадают');
        return;
      }
      // Подготовка данных для отправки
      if (this.form.password) {
        const userData = {password:
                          this.form.password}
        // Отправка запроса на обновление профиля
        this.changeUserData({user_id: this.user.id, userData})
          .then(() => {
            alert('Профиль обновлен');
            // При необходимости обновите информацию о пользователе в store
          })
          .catch(error => {
            console.error(error);
            alert('Ошибка при обновлении профиля');
          });
      }
    }
  }
};
</script>

<style scoped>
/* Стили для страницы профиля */
.profile-page {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.profile-form {
  background-color: #ffffff;
  padding: 40px 30px;
  border-radius: 8px;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.profile-form h2 {
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
</style>
