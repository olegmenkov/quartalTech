""""! @brief Описывает модели БД системы"""

##
# @file models.py 
#
# @brief Описывает модели БД системы.
#
# @section description_models Описание
# Описывает основные модели базы данных, используемые в работе системы.
# - Apartment
# - Listing
#
# @section libraries_models Используемые библиотеки/модули
# - sqlalchemy (https://www.sqlalchemy.org/)
#   - Набор инструментов для описания моделей БД.
#
# @section notes_models Заметки
# - Отсутствуют.
#
# @section todo_models TODO
# - Отсутствуют.
#
# @section author_models Author(s)
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.


from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Apartment(Base):
    """! Модель квартиры

    Описывает квартиру в БД 
    """

    ## Название таблицы
    __tablename__ = "apartments"

    ## Идентификатор квартиры: целое число и первичный ключ
    id = Column(Integer, primary_key=True, index=True)

    ## Название квартиры для отображения: строка
    name = Column(String, index=True)

    ## Площадь квартиры в кв.м.: дробное число
    area = Column(Float)

    ## Количество комнат в квартире: целое число
    rooms = Column(Integer)

    ## Оценочная стоимость квартиры: дробное число
    estimated_price = Column(Float)

    ## Предложения о продаже квартиры: связь с классом `Listing`
    listings = relationship("Listing", back_populates="apartment")


class Listing(Base):
    """! Модель предложения о продаже квартиры

    Описывает предложение о продаже в БД
    """

    ## Название таблицы
    __tablename__ = "listings"

    ## Идентификатор предложения: целое число, первичный ключ
    id = Column(Integer, primary_key=True, index=True)
    
    ## Источник, откуда было получено предложение: строка
    source = Column(String, index=True)
    
    ## Идентификатор квартиры, которую продают: внешний ключ к полю `id` таблицы `apartments`
    apartment_id = Column(Integer, ForeignKey("apartments.id"))

    ## Квартира, которую продают: связь с классом `Apartment`
    apartment = relationship("Apartment", back_populates="listings")
