<!-- src/components/PredictPrice.vue -->
<template>
  <div>
    <h2>Predict Apartment Price</h2>
    <form @submit.prevent="predictPrice">
      <label>Area:</label>
      <input v-model.number="area" type="number" required />

      <label>Rooms:</label>
      <input v-model.number="rooms" type="number" required />

      <button type="submit">Calculate</button>
    </form>
    <div v-if="price">
      <h3>Estimated Price: {{ price }}</h3>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const backendUrl = process.env.VUE_APP_BACKEND_URL || 'http://localhost:8000';

export default {
  data() {
    return {
      area: null,
      rooms: null,
      price: null
    };
  },
  methods: {
    predictPrice() {
      axios.get(`${backendUrl}/calculate/`, { params: { area: this.area, rooms: this.rooms } })
        .then(response => {
          this.price = response.data.price;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
/* Add styles for predict price form */
</style>
