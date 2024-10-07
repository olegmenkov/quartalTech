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
    predicted_price = 19*10**6
    return {"predicted_price": predicted_price}
