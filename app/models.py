from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from app.db_setup import Base
from enum import Enum as PyEnum


class UserRole(PyEnum):
    UNAUTHORIZED = "unauthorized"
    AUTHORIZED = "authorized"
    ADMIN = "admin"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.AUTHORIZED)


class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    area = Column(Float, nullable=False)
    rooms = Column(Integer, nullable=False)
    estimated_price = Column(Float, nullable=False)
