<!-- src/components/PredictPrice.vue -->
<template>
  <div class="predict-page">
    <div class="predict-container">
      <div class="form-section">
        <h2>Рассчитать стоимость квартиры</h2>
        <form @submit.prevent="onPredictPrice" class="predict-form">
          <div class="form-group">
            <label>Площадь (м²):</label>
            <input v-model.number="area" type="number" min="0" required />
          </div>
          <div class="form-group">
            <label>Количество комнат:</label>
            <input v-model.number="rooms" type="number" min="0" required />
          </div>
          <div class="form-group">
            <label>Этаж:</label>
            <input v-model.number="floor" type="number" min="0" required />
          </div>
          <div class="form-group">
            <label>Этажей в доме:</label>
            <input v-model.number="total_floors" type="number" min="0" required />
          </div>
          <div class="form-group">
            <label>Район:</label>
            <input v-model="district" type="text" />
          </div>
          <div class="form-group">
            <label>Ближайшее метро:</label>
            <input v-model="underground" type="text" />
          </div>
          <button type="submit" class="btn">Рассчитать</button>
        </form>
      </div>
      <div class="arrow-section">
        <span class="arrow">=&gt;</span>
      </div>
      <div class="result-section">
        <h3>Оценочная стоимость:</h3>
        <div v-if="price !== null">
          <p class="price">{{ formattedPrice }}</p>
        </div>
        <div v-else>
          <p class="no-price">Введите данные и нажмите "Рассчитать"</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      area: null,
      rooms: null,
      floor: null,
      total_floors: null,
      district: '',
      underground: ''
    };
  },
  computed: {
    // Map the price from the store
    ...mapGetters(['price']),
    formattedPrice() {
      console.log(this.price)
      if (this.price !== null) {
        return new Intl.NumberFormat('ru-RU', {
          style: 'currency',
          currency: 'RUB',
          maximumFractionDigits: 0
        }).format(this.price);
      }
      return '';
    }
  },
  methods: {
    // Map the predictPrice action from the store
    ...mapActions(['predictPrice']),
    onPredictPrice() {
      // Prepare parameters, excluding null or empty values
      console.log("RUn on predict price")
      const params = {};
      if (this.area !== null) params.area = this.area;
      if (this.rooms !== null) params.rooms = this.rooms;
      if (this.floor !== null) params.floor = this.floor;
      if (this.total_floors !== null) params.total_floors = this.total_floors;
      if (this.district !== '') params.district = this.district;
      if (this.underground !== '') params.underground = this.underground;

      this.predictPrice(params)
        .catch(error => {
          console.error(error);
          alert('Ошибка при расчете стоимости. Пожалуйста, попробуйте еще раз.');
        });
    }
  },
  created() {
    // Clear any previous price when the component is created
    this.$store.commit('SET_PREDICTED_PRICE', null);
  }
};
</script>

<style scoped>
/* Styles for the predict price page */
.predict-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px); /* Adjust if header height is different */
  background-color: #ecf0f1;
}

.predict-container {
  display: flex;
  align-items: center;
  background-color: #ffffff;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-section {
  max-width: 400px;
}

.predict-form .form-group {
  margin-bottom: 15px;
}

.predict-form .form-group label {
  display: block;
  color: #34495e;
  margin-bottom: 5px;
  font-weight: bold;
}

.predict-form .form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

.predict-form .form-group input:focus {
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
  margin-top: 10px;
}

.btn:hover {
  background-color: #16a085;
}

.arrow-section {
  margin: 0 30px;
  font-size: 36px;
  color: #2c3e50;
}

.result-section {
  max-width: 300px;
}

.result-section h3 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.price {
  font-size: 32px;
  font-weight: bold;
  color: #e74c3c;
}

.no-price {
  font-size: 16px;
  color: #7f8c8d;
}

@media (max-width: 768px) {
  .predict-container {
    flex-direction: column;
    padding: 20px;
  }

  .arrow-section {
    margin: 20px 0;
  }
}
</style>
