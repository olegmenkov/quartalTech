from fastapi import FastAPI
from app.routers import apartments, users, analytics, calculations
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="КварталТек", description="Веб-портал для анализа недвижимости.")

# Подключение роутеров
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(apartments.router, prefix="/apartments", tags=["Apartments"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(calculations.router, prefix="/calculate", tags=["Calculations"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешенные источники (можно использовать ["*"] для разрешения всех)
    allow_credentials=True,  # Разрешить отправку cookies/Authorization headers
    allow_methods=["*"],  # Разрешенные методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешенные заголовки
)

@app.get("/")
def root():
    return {"message": "Welcome to КварталТек!"}
