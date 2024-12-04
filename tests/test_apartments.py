import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db, get_test_db
from setup import setup_test_db

client = TestClient(app)

# Переопределяем зависимость на тестовую базу
app.dependency_overrides[get_db] = get_test_db


def test_create_apartment_admin(setup_test_db):
    # Регистрируем пользователя
    client.post(
        "/users/",
        json={"username": "test_user", "password": "test_password", "admin_key": "your_secret_key"}
    )
    # Логинимся
    response = client.post(
        "/users/login/",
        json={"username": "test_user", "password": "test_password"}
    )
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Создаём квартиру
    response = client.post(
        "/apartments/",
        json={"name": "Test Apartment", "area": 50.5, "rooms": 2, "price": 100000.0, "floor": 4, "total_floors": 10, "district": "Аэропорт", "underground": "Аэропорт"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Apartment"

def test_create_apartment_authorized(setup_test_db):
    # Регистрируем пользователя
    client.post(
        "/users/",
        json={"username": "test_user", "password": "test_password"}
    )
    # Логинимся
    response = client.post(
        "/users/login/",
        json={"username": "test_user", "password": "test_password"}
    )
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Создаём квартиру
    response = client.post(
        "/apartments/",
        json={"name": "Test Apartment", "area": 50.5, "rooms": 2, "price": 100000.0},
        headers=headers,
    )
    assert response.status_code == 403


def test_create_apartment_not_authorized(setup_test_db):
    # Создаём квартиру
    response = client.post(
        "/apartments/",
        json={"name": "Test Apartment", "area": 50.5, "rooms": 2, "price": 100000.0},
    )
    assert response.status_code == 401
