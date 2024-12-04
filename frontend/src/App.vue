<template>
  <div id="app">
    <header>
      <h1>КварталТек</h1>
      <nav>
        <router-link to="/">Главная</router-link>
        <button @click="navigateTo('/login')">Авторизация</button>
        <button @click="navigateTo('/register')">Регистрация</button>
        <router-link to="/apartments">Список квартир</router-link>
      </nav>
    </header>

    <main>
      <router-view />
    </main>

    <footer>
      <p>&copy; 2024 КварталТек. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    },
  },
};
</script>

<style>
/* Общие стили */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Шапка */
header {
  background-color: #343a40;
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header h1 {
  margin: 0;
  font-size: 1.5em;
}

nav {
  display: flex;
  gap: 15px;
}

nav a {
  color: white;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

/* Основная часть */
main {
  flex: 1;
  padding: 20px;
}

/* Подвал */
footer {
  background-color: #343a40;
  color: white;
  text-align: center;
  padding: 10px;
}
</style>
