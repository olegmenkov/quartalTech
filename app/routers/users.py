from fastapi import APIRouter, Depends, HTTPException
from passlib.handlers.bcrypt import bcrypt
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from app.auth import create_access_token, get_current_user
from app.models import User, UserRole
from app.schemas import UserResponse, UserCreate, UserLogin, UserInfo
from app.dependencies import get_db

router = APIRouter()

# Секретный ключ и параметры JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Создать нового пользователя
@router.post("/", response_model=dict)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Проверяем, существует ли пользователь
    result = db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Создаем нового пользователя
    hashed_password = bcrypt.hash(user.password)
    if user.admin_key:
        if user.admin_key == SECRET_KEY:
            new_user = User(username=user.username, hashed_password=hashed_password, role=UserRole.ADMIN)
        else:
            raise HTTPException(status_code=400, detail="Invalid admin key")
    else:
        new_user = User(username=user.username, hashed_password=hashed_password, role=UserRole.AUTHORIZED)

    db.add(new_user)
    db.commit()  # Сохраняем изменения
    db.refresh(new_user)  # Обновляем объект, чтобы получить значение id

    return {"username": new_user.username, "role": new_user.role}


# Логин пользователя и получение токена
@router.post("/login")
def login(
    input: UserLogin, db: Session = Depends(get_db)
):
    # Проверяем, существует ли пользователь
    result = db.execute(select(User).where(User.username == input.username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Проверяем пароль
    if not bcrypt.verify(input.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    print(user.id)
    # Генерируем токен
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer", "id": user.id}


@router.get("/")
def user(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Проверяем, существует ли пользователь
    if user:
        return {"id": user.id,
                "username": user.username,
                "role": user.role}
    else:
        raise HTTPException(status_code=404, detail="User not found")