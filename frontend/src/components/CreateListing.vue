<!-- src/components/CreateListing.vue -->
<template>
  <div>
    <h2>Create New Listing</h2>
    <form @submit.prevent="createListing">
      <label>Name:</label>
      <input v-model="form.name" required />

      <label>Area:</label>
      <input v-model.number="form.area" type="number" required />

      <label>Rooms:</label>
      <input v-model.number="form.rooms" type="number" required />

      <label>Price:</label>
      <input v-model.number="form.price" type="number" required />

      <label>Floor:</label>
      <input v-model.number="form.floor" type="number" required />

      <label>Total Floors:</label>
      <input v-model.number="form.total_floors" type="number" required />

      <label>District:</label>
      <input v-model="form.district" />

      <label>Underground:</label>
      <input v-model="form.underground" />

      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

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
        underground: ''
      }
    };
  },
  methods: {
    ...mapActions(['createApartment']),
    createListing() {
      this.createApartment(this.form)
        .then(() => {
          // Redirect or show success message
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
/* Add styles for create listing form */
</style>
