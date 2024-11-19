from sqlalchemy.orm import Session
from app.models import Apartment


def filter_apartments(db: Session, area_min: float = None, area_max: float = None,
                      rooms_min: int = None, rooms_max: int = None, price_min: float = None, price_max: float = None):
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

    return query.all()

