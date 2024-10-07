from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, database

router = APIRouter(
    prefix="/apartments",
    tags=["apartments"]
)


@router.get("/", response_model=List[schemas.Apartment])
async def get_apartments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(database.get_db)):
    result = await db.execute(select(models.Apartment).offset(skip).limit(limit))
    return result.scalars().all()


@router.post("/", response_model=schemas.Apartment)
async def create_apartment(apartment: schemas.ApartmentCreate, db: AsyncSession = Depends(database.get_db)):
    db_apartment = models.Apartment(**apartment.dict())
    db.add(db_apartment)
    await db.commit()
    await db.refresh(db_apartment)
    return db_apartment
