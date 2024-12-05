<!-- src/views/Home.vue -->
<template>
  <div>
    <ApartmentFilters />
    <ApartmentTable />
  </div>
</template>

<script>
import ApartmentFilters from '../components/ApartmentFilters.vue';
import ApartmentTable from '../components/ApartmentTable.vue';

export default {
  components: {
    ApartmentFilters,
    ApartmentTable
  }
};
</script>