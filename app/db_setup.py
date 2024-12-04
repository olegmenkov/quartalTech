from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@db/db"

engine = create_engine(DATABASE_URL, echo=True)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
print("Registered tables:", Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
