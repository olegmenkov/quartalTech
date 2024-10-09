"""! @brief Описывает схемы сущностей системы."""

##
# @file schemas.py 
#
# @brief Описывает схемы сущностей системы.
#
# @section description_schemas Описание
# Описывает базовые и основные схемы сущностей.
# - ListingBase (базовая)
# - ListingCreate
# - Listing
# - ApartmentBase (базовая)
# - ApartmentCreate
# - Apartment
#
# @section libraries_schemas Используемые библиотеки/модули
# - pydantic (https://docs.pydantic.dev/latest/)
#   - Доступ к базовой схеме.
#
# @section notes_schemas Заметки
# - Отсутствуют.
#
# @section todo_sensors TODO
# - Отсутствуют.
#
# @section author_sensors Author(s)
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.

from pydantic import BaseModel, ConfigDict 
from typing import List, Optional


class ListingBase(BaseModel):
    """! Базовая схема предложения о продаже

    Описывает предложение о продаже квартиры, полученное
    из какого-либо аггрегатора
    """

    ## Источник 
    source: str


class ListingCreate(ListingBase):
    """! Класс создания предложения о квартире
    """
    pass


class Listing(ListingBase):
    """! Схема предложения о продаже

    Включает в себя информацию о связи с квартирой
    """

    ## Конфигурация ORM для pydantic
    model_config = ConfigDict(from_attributes=True)

    ## Идентификатор записи
    id: int

    ## Ссылка на квартиру, которую продают
    apartment_id: int


class ApartmentBase(BaseModel):
    """! Базовая схема квартиры

    Определяет все свойства любой квартиры 
    """

    ## Название квартиры для отображения
    name: str

    ## Площадь квартиры в кв.м.
    area: float

    ## Количество комнат в квартире
    rooms: int


class ApartmentCreate(ApartmentBase):
    """! Класс создания квартиры
    """
    pass


class Apartment(ApartmentBase):
    """! Класс квартиры в системе

    Содержит свойства квартиры, используемые в системе
    """

    ## Конфигурация ORM для pydantic
    model_config = ConfigDict(from_attributes=True)

    ## Идентификатор записи в БД
    id: int

    ## Оценочная стоимость квартиры в руб.
    estimated_price: Optional[float] = None

    ## Список предложений о продаже данной квартиры
    listings: List[Listing] = []

