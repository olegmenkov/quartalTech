# Stage 1: Build the Vue.js application
FROM node:16-alpine AS build-stage

WORKDIR /app

# Copy package.json and package-lock.json if available
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the built files using nginx
FROM nginx:stable-alpine AS production-stage

# Copy the built files from the previous stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy nginx configuration if needed
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
