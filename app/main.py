from fastapi import FastAPI
from app.routers import apartments, neural_network
from app.database import engine
from app.models import Base


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app = FastAPI()

app.include_router(apartments.router)
app.include_router(neural_network.router)


@app.on_event("startup")
async def on_startup():
    await create_tables()


@app.get("/")
async def root():
    return {"message": "Welcome to QuartalTek!"}
