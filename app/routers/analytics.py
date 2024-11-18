from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.analytics import analyze_price_trends
from app.dependencies import get_db

router = APIRouter()


@router.get("/price-trends")
def price_trends(db: Session = Depends(get_db)):
    return analyze_price_trends(db)
