from pydantic import BaseModel
from typing import List, Optional


class ListingBase(BaseModel):
    source: str


class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int
    apartment_id: int

    class Config:
        orm_mode = True


class ApartmentBase(BaseModel):
    name: str
    area: float
    rooms: int


class ApartmentCreate(ApartmentBase):
    pass


class Apartment(ApartmentBase):
    id: int
    estimated_price: Optional[float] = None
    listings: List[Listing] = []

    class Config:
        orm_mode = True
