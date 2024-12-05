<!-- src/components/CreateListing.vue -->
<template>
  <div class="create-listing-page">
    <div class="create-listing-form">
      <h2>Создать объявление</h2>
      <form @submit.prevent="createListing">
        <div class="form-group">
          <label for="name">Название:</label>
          <input id="name" v-model="form.name" required />
        </div>

        <div class="form-group">
          <label for="area">Площадь (м²):</label>
          <input id="area" v-model.number="form.area" type="number" min="0" required />
        </div>

        <div class="form-group">
          <label for="rooms">Количество комнат:</label>
          <input id="rooms" v-model.number="form.rooms" type="number" min="0" required />
        </div>

        <div class="form-group">
          <label for="price">Цена (₽):</label>
          <input id="price" v-model.number="form.price" type="number" min="0" required />
        </div>

        <div class="form-group">
          <label for="floor">Этаж:</label>
          <input id="floor" v-model.number="form.floor" type="number" min="0" required />
        </div>

        <div class="form-group">
          <label for="total_floors">Этажей в доме:</label>
          <input id="total_floors" v-model.number="form.total_floors" type="number" min="0" required />
        </div>

        <div class="form-group">
          <label for="district">Район:</label>
          <input id="district" v-model="form.district" required />
        </div>

        <div class="form-group">
          <label for="underground">Метро:</label>
          <input id="underground" v-model="form.underground" />
        </div>

        <div class="form-group">
          <label for="fio">ФИО контактного лица:</label>
          <input id="fio" v-model="form.fio" required />
        </div>

        <div class="form-group">
          <label for="phone">Телефон:</label>
          <input id="phone" v-model="form.phone" required />
        </div>

        <div class="form-group">
          <label for="email">Email:</label>
          <input id="email" v-model="form.email" type="email" required />
        </div>

        <button type="submit" class="btn">Создать объявление</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        area: null,
        rooms: null,
        price: null,
        floor: null,
        total_floors: null,
        district: '',
        underground: '',
        fio: '',
        phone: '',
        email: ''
      }
    };
  },
  methods: {
    createListing() {
      this.$store.dispatch('createApartment', this.form)
        .then(() => {
          // Сообщение об успешном создании и перенаправление
          alert('Объявление успешно создано');
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
          alert('Ошибка при создании объявления');
        });
    }
  }
};
</script>

<style scoped>
/* Стили для страницы создания объявления */
.create-listing-page {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.create-listing-form {
  background-color: #ffffff;
  padding: 40px 30px;
  border-radius: 8px;
  max-width: 600px;
  width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.create-listing-form h2 {
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
