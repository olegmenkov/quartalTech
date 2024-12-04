import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db, get_test_db
from app.dependencies import Base, test_engine
from setup import setup_test_db
client = TestClient(app)

# Переопределяем зависимость на тестовую базу
app.dependency_overrides[get_db] = get_test_db


def test_user_registration(setup_test_db):
    response = client.post(
        "/users/",
        json={"username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"


def test_user_login(setup_test_db):
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
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_admin_login(setup_test_db):
    # Регистрируем пользователя
    response = client.post(
        "/users/",
        json={"username": "test_user", "password": "test_password", "admin_key": "your_secret_key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "admin"
    # Логинимся
    response = client.post(
        "/users/login/",
        json={"username": "test_user", "password": "test_password"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
