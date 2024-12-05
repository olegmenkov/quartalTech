<!-- src/components/ApartmentFilters.vue -->
<template>
  <div>
    <form @submit.prevent="applyFilters">
      <label>Area Min:</label>
      <input v-model.number="filters.area_min" type="number" :disabled="!isLoggedIn" />

      <label>Area Max:</label>
      <input v-model.number="filters.area_max" type="number" :disabled="!isLoggedIn" />

      <!-- Add more filters as needed -->

      <button type="submit" :disabled="!isLoggedIn">Apply Filters</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      filters: {
        area_min: null,
        area_max: null,
        // Initialize other filters
      }
    };
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
    ...mapActions(['fetchApartments']),
    applyFilters() {
      this.fetchApartments(this.filters);
    }
  }
};
</script>

<style scoped>
/* Add styles for filters */
</style>