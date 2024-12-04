# Стадия сборки
FROM node:16 as build

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY package*.json ./

# Устанавливаем зависимости, включая devDependencies
RUN npm install

# Устанавливаем отсутствующий парсер ESLint
RUN npm install --save-dev @babel/eslint-parser \
npm install cors
# Копируем все файлы проекта
COPY . .

# Сборка проекта
RUN npm run build

# Стадия сервера
FROM nginx:stable-alpine

# Копируем собранный фронтенд в директорию Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем кастомную конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Экспонируем порт
EXPOSE 80

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]
