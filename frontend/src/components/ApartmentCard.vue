<template>
  <div class="card animate__animated animate__zoomIn">
    <h3>{{ apartment.name }}</h3>
    <p>Площадь: {{ apartment.area }} м²</p>
    <p>Комнаты: {{ apartment.rooms }}</p>
    <p>Цена: {{ apartment.estimated_price }} ₽</p>
  </div>
</template>

<script>
export default {
  props: ['apartment'],
};
</script>

<style scoped>
.card {
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fafafa;
  width: 250px;
}
</style>
