from sqlalchemy.orm import Session
from app.models import Apartment


def filter_apartments(db: Session, area_min: float = None, area_max: float = None,
                      rooms_min: int = None, rooms_max: int = None, price_min: float = None, price_max: float = None,
                      floor_min: int = None, floor_max: int = None, total_floors_min: int = None,
                      total_floors_max: int = None, district: str = None, underground: str = None
                      ):
    query = db.query(Apartment)

    if area_min is not None:
        query = query.filter(Apartment.area >= area_min)
    if area_max is not None:
        query = query.filter(Apartment.area <= area_max)
    if rooms_min is not None:
        query = query.filter(Apartment.rooms >= rooms_min)
    if rooms_max is not None:
        query = query.filter(Apartment.rooms <= rooms_max)
    if price_min is not None:
        query = query.filter(Apartment.estimated_price >= price_min)
    if price_max is not None:
        query = query.filter(Apartment.estimated_price <= price_max)
    if floor_max is not None:
        query = query.filter(Apartment.floors <= floor_max)
    if floor_min is not None:
        query = query.filter(Apartment.floors >= floor_min)
    if total_floors_min is not None:
        query = query.filter(Apartment.floors >= total_floors_min)
    if total_floors_max is not None:
        query = query.filter(Apartment.floors <= total_floors_max)
    if district is not None:
        query = query.filter(Apartment.district == district)
    if underground is not None:
        query = query.filter(Apartment.underground == underground)


    return query.all()

