// vue.config.js
module.exports = {
  // Ваши конфигурации
  devServer: {
    proxy: {
      "/api": {
        target: "http://app:8000", // Проксируем запросы на API
        changeOrigin: true,
      },
    },
  },
};
