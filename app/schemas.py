from pydantic import BaseModel


# Общая схема для пользователя
class UserBase(BaseModel):
    username: str


# Схема для ответа пользователя (включает ID)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# Схема для создания нового пользователя
class UserCreateOrLogin(UserBase):
    password: str  # Добавляем поле пароля


