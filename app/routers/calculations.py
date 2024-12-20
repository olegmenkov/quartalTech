from fastapi import APIRouter, Depends

from app.schemas import ApartmentInfo
from app.services.pricing import calculate_price
from app.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=dict)
def calculate(area: float | None = None, rooms: int | None = None, floor: int | None = None,
              total_floors: int | None = None,district: str | None = None, underground: str | None = None,
              user=Depends(get_current_user)):
    price = calculate_price(area, rooms, floor, total_floors, district, underground)
    return {"price": price}
