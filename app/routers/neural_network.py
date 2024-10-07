from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/neural_network",
    tags=["neural_network"]
)


class PricePredictionRequest(BaseModel):
    area: float
    rooms: int


@router.post("/predict")
async def predict_price(data: PricePredictionRequest):
    # здесь будет логика нейронки
    return {"predicted_price": 12*10**6}
