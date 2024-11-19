from typing import Optional

from pydantic import BaseModel


# Общая схема для пользователя
class UserBase(BaseModel):
    username: str


# Схема для ответа о пользователе
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserLogin(UserBase):
    password: str


class UserCreate(UserLogin):
    admin_key: Optional[str] = None


class UserInfo(UserResponse):
    role: str


class ApartmentInfo(BaseModel):
    name: str
    area: float
    rooms: int
    price: float


class ApartmentFilter(BaseModel):
    area_min: Optional[float] = None
    area_max: Optional[float] = None
    rooms_min: Optional[int] = None
    rooms_max: Optional[int] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None


class ApartmentResponse(BaseModel):
    id: int
    name: str
    area: float
    rooms: int
    estimated_price: float

    class Config:
        from_attributes = True
