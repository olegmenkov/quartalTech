import logging

from fastapi import APIRouter, Depends, Query, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.auth import get_current_user, get_admin_user
from app.dependencies import get_db
from app.services.filters import filter_apartments
from app.schemas import ApartmentResponse, ApartmentFilter, ApartmentInfo
from app.models import Apartment

router = APIRouter()


@router.get("/", response_model=list[ApartmentResponse])
def get_apartments(area_min: float = Query(None, description="Минимальная площадь"),
                   area_max: float = Query(None, description="Максимальная площадь"),
                   rooms_min: int = Query(None, description="Минимальное количество комнат"),
                   rooms_max: int = Query(None, description="Максимальное количество комнат"),
                   price_min: float = Query(None, description="Минимальная цена"),
                   price_max: float = Query(None, description="Максимальная цена"),
                   floor_min: int = Query(None, description="Самый низкий этаж"),
                   floor_max: int = Query(None, description="Самый высокий этаж"),
                   total_floors_min: int = Query(None, description="Минимальное количество этажей в доме"),
                   total_floors_max: int = Query(None, description="Максимальное количество этажей в доме"),
                   district: str = Query(None, description="Район"),
                   underground: str = Query(None, description="Станция метро"),
                   db: Session = Depends(get_db),
                   ):
    """
    Получить список квартир с фильтрами. Фильтры могут быть применены по одному или нескольким полям.
    """
    apartments = filter_apartments(
        db, area_min=area_min, area_max=area_max, rooms_min=rooms_min, rooms_max=rooms_max, price_min=price_min,
        price_max=price_max, floor_max=floor_max, floor_min=floor_min, total_floors_min=total_floors_min, total_floors_max=total_floors_max,
        district=district, underground=underground
    )
    return apartments




@router.post("/", response_model=ApartmentResponse)
def create_apartment(input: ApartmentInfo, User: str = Depends(get_admin_user), db: Session = Depends(get_db)):
    new_apartment = Apartment(name=input.name,
                              area=input.area,
                              rooms=input.rooms,
                              estimated_price=input.price,
                              floor=input.floor,
                              total_floors=input.total_floors,
                              district=input.district,
                              underground=input.underground,
                              fio=input.fio,
                              phone=input.phone,
                              email=input.email,
                            )
    db.add(new_apartment)
    db.commit()  # Сохраняем изменения
    db.refresh(new_apartment)  # Обновляем объект, чтобы получить значение id
    return new_apartment
