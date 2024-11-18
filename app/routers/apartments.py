from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import get_admin_user
from app.models import Apartment
from app.schemas import ApartmentResponse, ApartmentCreate
from app.dependencies import get_db

router = APIRouter()


# Получить список квартир
@router.get("/", response_model=list[ApartmentResponse])
def list_apartments(filter: str = None, db: Session = Depends(get_db)):
    query = db.query(Apartment)
    if filter:
        query = query.filter(Apartment.name.ilike(f"%{filter}%"))
    apartments = query.all()
    return apartments


@router.post("/")
def create_apartment(apartment: ApartmentCreate, db: Session = Depends(get_db), admin=Depends(get_admin_user)):
    db.add(apartment)
    db.commit()
    db.refresh(apartment)
    return {"message": "Apartment added", "apartment": apartment}
