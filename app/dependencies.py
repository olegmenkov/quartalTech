from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db_setup import SessionLocal, Base


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Тестовая база PostgreSQL
TEST_DATABASE_URL = "postgresql+psycopg2://test_user:test_password@localhost:5433/test_db"

test_engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_test_db():
    # Создание таблиц для теста
    Base.metadata.create_all(bind=test_engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
