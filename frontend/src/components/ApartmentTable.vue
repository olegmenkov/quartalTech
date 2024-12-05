<!-- src/components/ApartmentTable.vue -->
<template>
  <div class="apartment-table-container">
    <table class="apartment-table">
      <thead>
        <tr>
          <th>Название</th>
          <th>Площадь (м²)</th>
          <th>Комнат</th>
          <th>Цена (₽)</th>
          <th>Этаж</th>
          <th>Этажей в доме</th>
          <th>Район</th>
          <th>Метро</th>
          <!-- Добавьте дополнительные столбцы по необходимости -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="apartment in apartments" :key="apartment.id" @click="selectApartment(apartment)">
          <td>{{ apartment.name }}</td>
          <td>{{ apartment.area }}</td>
          <td>{{ apartment.rooms }}</td>
          <td>{{ apartment.estimated_price }}</td>
          <td>{{ apartment.floor }}</td>
          <td>{{ apartment.total_floors }}</td>
          <td>{{ apartment.district }}</td>
          <td>{{ apartment.underground }}</td>
          <!-- Отобразите дополнительные данные по необходимости -->
        </tr>
      </tbody>
    </table>
    <!-- Элементы управления пагинацией могут быть добавлены здесь -->
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
      // Обновляем список квартир
      this.$store.dispatch('fetchApartments');
    }
  }
};
</script>

<style scoped>
/* Стили для таблицы */
.apartment-table-container {
  overflow-x: auto;
}

.apartment-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.apartment-table th,
.apartment-table td {
  border: 1px solid #ddd;
  padding: 8px;
}

.apartment-table th {
  background-color: #f2f2f2;
  color: #2c3e50;
  text-align: left;
}

.apartment-table tr:hover {
  background-color: #f1f1f1;
  cursor: pointer;
}
</style>
