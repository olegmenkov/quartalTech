"""! @brief Содержит обработчик HTTP запросов о квартирах."""

##
# @file routers/apartments.py 
#
# @brief Содержит обработчик HTTP запросов о квартирах. 
#
# @section description_routers_apartments Описание
# Содержит основные обработчики HTTP запросов о квартирах.
# - get_apartments - получение списка квартир
# - create_apartment - создание квартиры
#  
# @section libraries_routers_apartments Используемые библиотеки/модули
# - sqlalchemy (https://www.sqlalchemy.org/)
#   - Набор инструментов для создания БД.
# - os standard library (https://docs.python.org/3/library/os.html)
# - dotenv (https://pypi.org/project/python-dotenv/)
#   - load_dotenv читает системные переменные среды из файла .env
# 
# @section notes_routers_apartments Заметки
# - Отсутствуют.
#
# @section todo_routers_apartments TODO
# - Отсутствуют.
#
# @section author_routers_apartments Author(s)
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, database

## Настройка пути запроса: /apartments
router = APIRouter(
    prefix="/apartments",
    tags=["apartments"]
)


@router.get("/", response_model=List[schemas.Apartment])
async def get_apartments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    """! Получение списка квартир

    @param skip  Сколько записей с начала таблицы пропустить
    @param limit Сколько записей из запроса вернуть
    @param db    Сессия БД

    @return Полученный список квартир
    """
    result = await db.execute(select(models.Apartment).offset(skip).limit(limit))
    return result.scalars().all()


@router.post("/", response_model=schemas.Apartment)
async def create_apartment(apartment: schemas.ApartmentCreate, db: AsyncSession = Depends(database.get_db)):
    """! Создание квартиры

    @param apartment Контейнер данных о квартире
    @param db        Сессия БД

    @return Созданная квартира
    """
    db_apartment = models.Apartment(**apartment.dict())
    db.add(db_apartment)
    await db.commit()
    await db.refresh(db_apartment)
    return db_apartment
