import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db, get_test_db
from app.dependencies import Base, test_engine

client = TestClient(app)

# Переопределяем зависимость на тестовую базу
app.dependency_overrides[get_db] = get_test_db


@pytest.fixture
def setup_test_db():
    # Удаляем и создаем тестовые таблицы
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    yield