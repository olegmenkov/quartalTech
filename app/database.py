"""! @brief Содержит код конфигурации и запуска БД."""

##
# @file database.py 
#
# @brief Содержит код конфигурации и запуска БД.
#
# @section description_database Описание
# Читает конфигурацию БД из системных переменных среды и запускает БД
#
# @section libraries_database Используемые библиотеки/модули
# - sqlalchemy (https://www.sqlalchemy.org/)
#   - Набор инструментов для создания БД.
# - os standard library (https://docs.python.org/3/library/os.html)
# - dotenv (https://pypi.org/project/python-dotenv/)
#   - load_dotenv читает системные переменные среды из файла .env
# 
# @section notes_database Заметки
# - Отсутствуют.
#
# @section todo_database TODO
# - Отсутствуют.
#
# @section author_database Author(s)
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

## URL Базы данных
DATABASE_URL = os.getenv("DATABASE_URL")

## Создание подключения к БД
engine = create_async_engine(DATABASE_URL, echo=True)

## Сессия подключения к БД
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


async def get_db():
    """! Реализует получение сессии БД.

    @return Генератор сессий
    """
    async with AsyncSessionLocal() as session:
        yield session
