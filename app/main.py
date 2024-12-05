from fastapi import FastAPI
from app.routers import apartments, users, analytics, calculations
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Query, HTTPException, Request


app = FastAPI(title="КварталТек", description="Веб-портал для анализа недвижимости.")

# Подключение роутеров
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(apartments.router, prefix="/apartments", tags=["Apartments"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(calculations.router, prefix="/calculate", tags=["Calculations"])

@app.get("/")
def root():
    return {"message": "Welcome to КварталТек!"}

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "detail": [
                {
                    "loc": error["loc"],
                    "msg": error["msg"],
                    "type": error["type"],
                }
                for error in exc.errors()
            ]
        },
    )