<!-- src/components/Footer.vue -->
<template>
  <footer class="footer">
    <div class="container">
      <p>&copy; 2024 КварталТек. Все права защищены.</p>
      <p>
        <a href="/privacy-policy">Политика конфиденциальности</a> |
        <a href="/terms-of-service">Условия использования</a>
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
};
</script>

<style scoped>
.footer {
  background-color: #f8f9fa;
  padding: 20px 0;
  text-align: center;
  margin-top: auto;
}

.footer .container p {
  margin: 0;
  color: #6c757d;
}

.footer .container a {
  color: #007bff;
  text-decoration: none;
}

.footer .container a:hover {
  text-decoration: underline;
}
</style>