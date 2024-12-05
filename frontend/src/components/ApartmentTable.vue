<!-- src/components/ApartmentTable.vue -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Area</th>
          <th>Rooms</th>
          <th>Price</th>
          <th>Floor</th>
          <th>District</th>
          <!-- Add more columns as needed -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="apartment in apartments" :key="apartment.id" @click="selectApartment(apartment)">
          <td>{{ apartment.name }}</td>
          <td>{{ apartment.area }}</td>
          <td>{{ apartment.rooms }}</td>
          <td>{{ apartment.estimated_price }}</td>
          <td>{{ apartment.floor }}/{{ apartment.total_floors }}</td>
          <td>{{ apartment.district }}</td>
          <!-- Add more data as needed -->
        </tr>
      </tbody>
    </table>
    <!-- Pagination controls could be added here -->
    <EditApartment v-if="showEdit" :apartment="selectedApartment" @close="closeEdit" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import EditApartment from './EditApartment.vue';

export default {
  components: {
    EditApartment
  },
  data() {
    return {
      selectedApartment: null,
      showEdit: false
    };
  },
  computed: {
    ...mapGetters(['apartments', 'isAdmin'])
  },
  methods: {
    selectApartment(apartment) {
      if (this.isAdmin) {
        this.selectedApartment = apartment;
        this.showEdit = true;
      }
    },
    closeEdit() {
      this.showEdit = false;
      this.selectedApartment = null;
      // Refresh the apartments list
      this.$store.dispatch('fetchApartments');
    }
  }
};
</script>

<style scoped>
/* Add styles for the table */
</style>