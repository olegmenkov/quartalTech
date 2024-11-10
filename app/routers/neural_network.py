"""! @brief Содержит обработчик HTTP запросов для оценки стоимости квартиры."""

##
# @file routers/apartments.py 
#
# @brief Содержит обработчик HTTP запросов для оценки стоимости квартиры. 
#
# @section description_routers_neural_network Описание
# Содержит обработчик HTTP запросов для оценки стоимости квартиры.
# - predict_price - предсказывание цены квартиры 
#  
# @section libraries_routers_neural_network Используемые библиотеки/модули
# - fastapi (https://fastapi.tiangolo.com/)
#   - Библиотека для создания серверных приложений
# - pydantic (https://docs.pydantic.dev/latest/)
#   - Доступ к базовой схеме. 
#
# @section notes_routers_neural_network Заметки
# - Отсутствуют.
#
# @section todo_routers_neural_network TODO
# - Отсутствуют.
#
# @section author_routers_neural_network Создатели
# - Создан: Меньков Олег Георгиевич 07/10/2024
# - Изменен: Задерей Петр Алексеевич 09/10/2024..
#
# Copyright (c) 2024 HSE MIEM. All rights reserved.


from fastapi import APIRouter
from pydantic import BaseModel

## Настройка пути запроса: /neural_network.
router = APIRouter(
    prefix="/neural_network",
    tags=["neural_network"]
)


class PricePredictionRequest(BaseModel):
    """! Класс запроса на предсказание цены.

    Содержит информацию о квартире.
    """

    ## Площадь квартиры в квадратных м.
    area: float

    ## Кол-во комнат в квартире.
    rooms: int


@router.post("/predict")
async def predict_price(data: PricePredictionRequest):
    """! Предсказание цены квартиры.

    @param data Объект с информацией о квартире.
    
    @return Объект с информацией о цене.
    """
    # здесь будет логика нейронки
    # я что-то поменял ещё раз
    return {"predicted_price": 15*10**60}
