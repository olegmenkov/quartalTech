<!-- src/components/Profile.vue -->
<template>
  <div>
    <h2>Profile</h2>
    <form @submit.prevent="updateProfile">
      <label>Username:</label>
      <input v-model="form.username" required disabled />

      <label>Password:</label>
      <input v-model="form.password" type="password" />

      <label>Repeat Password:</label>
      <input v-model="form.password2" type="password" />

      <!-- Add more fields as needed -->

      <button type="submit">Update Profile</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

const backendUrl = process.env.VUE_APP_BACKEND_URL || 'http://localhost:8000';

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
    ...mapState(['user'])
  },
  created() {
    this.form.username = this.user.username;
  },
  methods: {
    updateProfile() {
      if (this.form.password !== this.form.password2) {
        alert("Passwords do not match");
        return;
      }
      // Send update request to backend
      axios.put(`${backendUrl}/users/${this.user.id}`, {
        password: this.form.password
        // Add more fields as needed
      })
      .then(() => {
        alert("Profile updated");
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
};
</script>

<style scoped>
/* Add styles for profile */
</style>
