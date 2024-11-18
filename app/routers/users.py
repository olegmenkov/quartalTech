from fastapi import APIRouter, Depends, HTTPException
from passlib.handlers.bcrypt import bcrypt
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import create_access_token
from app.models import User
from app.schemas import UserResponse, UserCreateOrLogin
from app.dependencies import get_db

router = APIRouter()

# Секретный ключ и параметры JWT
SECRET_KEY = "your_secret_key"  # Поменяйте на ваш секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Создать нового пользователя
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreateOrLogin, db: Session = Depends(get_db)):
    # Проверяем, существует ли пользователь
    result = db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Создаем нового пользователя
    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()  # Сохраняем изменения
    db.refresh(new_user)  # Обновляем объект, чтобы получить значение id

    return new_user


# Логин пользователя и получение токена
@router.post("/login")
def login(
    input: UserCreateOrLogin, db: Session = Depends(get_db)
):
    # Проверяем, существует ли пользователь
    result = db.execute(select(User).where(User.username == input.username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    # Проверяем пароль
    if not bcrypt.verify(input.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Генерируем токен
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
