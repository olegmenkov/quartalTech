<!-- src/components/ApartmentFilters.vue -->
<template>
  <div class="filters-container" v-if="isLoggedIn">
    <form @submit.prevent="applyFilters" class="filters-form">
      <h3>Фильтры</h3>

      <div class="filters-row">
        <div class="form-group">
          <label>Площадь от (м²):</label>
          <input v-model.number="filters.area_min" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Площадь до (м²):</label>
          <input v-model.number="filters.area_max" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Комнат от:</label>
          <input v-model.number="filters.rooms_min" type="number" min="0" />
        </div>
      </div>

      <div class="filters-row">
        <div class="form-group">
          <label>Комнат до:</label>
          <input v-model.number="filters.rooms_max" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Цена от (₽):</label>
          <input v-model.number="filters.price_min" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Цена до (₽):</label>
          <input v-model.number="filters.price_max" type="number" min="0" />
        </div>
      </div>

      <div class="filters-row">
        <div class="form-group">
          <label>Этаж от:</label>
          <input v-model.number="filters.floor_min" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Этаж до:</label>
          <input v-model.number="filters.floor_max" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Этажей в доме от:</label>
          <input v-model.number="filters.total_floors_min" type="number" min="0" />
        </div>
      </div>

      <div class="filters-row">
        <div class="form-group">
          <label>Этажей в доме до:</label>
          <input v-model.number="filters.total_floors_max" type="number" min="0" />
        </div>
        <div class="form-group">
          <label>Район:</label>
          <input v-model="filters.district" type="text" />
        </div>
        <div class="form-group">
          <label>Метро:</label>
          <input v-model="filters.underground" type="text" />
        </div>
      </div>

      <button type="submit" class="btn">Применить фильтры</button>
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
        rooms_min: null,
        rooms_max: null,
        price_min: null,
        price_max: null,
        floor_min: null,
        floor_max: null,
        total_floors_min: null,
        total_floors_max: null,
        district: '',
        underground: ''
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
/* Стили для фильтров */
.filters-container {
  background-color: #ffffff;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
}

.filters-form h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.filters-row {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 15px;
}

.filters-row .form-group {
  flex: 1 1 calc(33.333% - 10px);
  margin-right: 15px;
}

.filters-row .form-group:nth-child(3n) {
  margin-right: 0;
}

.form-group label {
  display: block;
  color: #34495e;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
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
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  background-color: #16a085;
}
</style>
