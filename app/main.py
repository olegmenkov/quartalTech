"""! @brief Серверное приложение системы о продаже и оценивании квартир"""
##
# @mainpage Серверное приложение системы о продаже и оценивании стоимости квартир
#
# @section description_mainpage Описание
# Приложение содержит описание схем и моделей БД системы, а также
# обработчиков для REST HTTP API  
#
# @section notes_mainpage Заметки
# - Система создается в рамках академического проекта по дисциплине "Технологии Разработки Программного Обеспечения"
#
# @section authors_mainpage Создатели системы
# - Меньков Олег Георгиевич
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.

##
# @file main.py
#
# @brief Содержит скрипт запуска приложения.
#
# @section description_main Описание
# Содержит скрипт запуска приложения.
#
# @section libraries_main Используемые библиотеки/модули
# - fastapi (https://fastapi.tiangolo.com/)
#   - Библиотека для создания серверных приложений
# - модуль routers (./routers)
#   - apartments - контроллер запросов на получение информации о квартирах
#   - neural_network - контроллер запросов к нейронной сети для оценки стоимости квартиры
# - модуль database (локальный)
#   - engine - инициализатор БД
# - модуль models (локальный)
#   - Base - базовый класс БД
#
# @section notes_main Заметки 
# - Отсутствуют.
#
# @section todo_main TODO
# - Отсутствуют.
#
# @section author_main Author(s)
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.

from fastapi import FastAPI
from app.routers import apartments, neural_network
from app.database import engine
from app.models import Base


async def create_tables():
    """! Создает в БД описанные таблицы
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


## Приложение FastAPI 
app = FastAPI()

app.include_router(apartments.router)
app.include_router(neural_network.router)


@app.on_event("startup")
async def on_startup():
    """! Подписчик события `startup`

    Создает таблицы при получении события
    """
    await create_tables()


@app.get("/")
async def root():
    """! Главная страница приложения
    """
    return {"message": "Welcome to QuartalTek!"}
