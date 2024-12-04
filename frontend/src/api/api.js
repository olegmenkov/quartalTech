import { API_BASE_URL } from '../config';

/**
 * Обрабатывает ответ сервера
 * @param {Response} response
 * @returns {Promise<any>}
 */
async function handleResponse(response) {
  if (response.ok) {
    const data = await response.json();
    console.log("Success:", data);
    return data;
  } else if (response.status === 400) {
    const error = await response.json();
    console.error("Bad Request:", error);
    return null;
  } else if (response.status === 401) {
    console.error("Unauthorized: Check your credentials.");
    return null;
  } else if (response.status === 500) {
    console.error("Server Error: Try again later.");
    return null;
  } else {
    console.error(`Unexpected status code ${response.status}:`, await response.text());
    return null;
  }
}

// Пример: Запрос на логин
export async function login(username, password) {
  try {
    const response = await fetch(`${BASE_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });
    return await handleResponse(response);
  } catch (error) {
    console.error("Error during login request:", error);
    return null;
  }
}

// Пример: Получение списка данных
export async function getData(endpoint) {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    return await handleResponse(response);
  } catch (error) {
    console.error(`Error during GET request to ${endpoint}:`, error);
    return null;
  }
}

// Пример: Создание новой записи
export async function createRecord(endpoint, payload) {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    return await handleResponse(response);
  } catch (error) {
    console.error(`Error during POST request to ${endpoint}:`, error);
    return null;
  }
}

// Пример: Удаление записи
export async function deleteRecord(endpoint, id) {
  try {
    const response = await fetch(`${BASE_URL}/${endpoint}/${id}`, {
      method: "DELETE",
    });
    return await handleResponse(response);
  } catch (error) {
    console.error(`Error during DELETE request to ${endpoint}/${id}:`, error);
    return null;
  }
}