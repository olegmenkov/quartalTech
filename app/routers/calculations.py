from fastapi import APIRouter, Depends
from app.services.pricing import calculate_price
from app.auth import get_current_user

router = APIRouter()


@router.post("/")
def calculate(apartment_id: int, user=Depends(get_current_user)):
    return calculate_price(apartment_id)
