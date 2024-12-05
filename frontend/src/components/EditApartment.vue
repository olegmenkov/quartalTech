<!-- src/components/EditApartment.vue -->
<template>
  <div class="modal">
    <div class="modal-content">
      <h2>Edit Apartment</h2>
      <form @submit.prevent="save">
        <label>Name:</label>
        <input v-model="form.name" required />

        <label>Area:</label>
        <input v-model.number="form.area" type="number" required />

        <label>Rooms:</label>
        <input v-model.number="form.rooms" type="number" required />

        <!-- Add more fields as needed -->

        <button type="submit">Save</button>
        <button type="button" @click="$emit('close')">Close</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const backendUrl = process.env.VUE_APP_BACKEND_URL || 'http://localhost:8000';

export default {
  props: ['apartment'],
  data() {
    return {
      form: { ...this.apartment }
    };
  },
  methods: {
    save() {
      axios.put(`${backendUrl}/apartments/${this.form.id}`, this.form)
        .then(() => {
          this.$emit('close');
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
/* Add styles for modal */
</style>