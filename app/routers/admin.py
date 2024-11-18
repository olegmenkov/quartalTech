from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ApartmentResponse
from app.auth import get_admin_user
from app.dependencies import get_db

router = APIRouter()



