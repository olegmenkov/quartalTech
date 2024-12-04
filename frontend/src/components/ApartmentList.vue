<template>
  <div class="apartment-list animate__animated animate__fadeIn">
    <h1>Список квартир</h1>
    <div class="apartment-card" v-for="apartment in apartments" :key="apartment.id">
      <ApartmentCard :apartment="apartment" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ApartmentCard from './ApartmentCard.vue';

export default {
  components: { ApartmentCard },
  data() {
    return {
      apartments: [],
    };
  },
  async mounted() {
    const response = await axios.get('http://localhost:8000/apartments', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    });
    this.apartments = response.data;
  },
};
</script>

<style scoped>
.apartment-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
</style>
