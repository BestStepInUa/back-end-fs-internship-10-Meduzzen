import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from app.config import settings

from app.routers import base_router


# asynccontextmanager
async def lifespan(app: FastAPI):
   yield
   print("Server is down :(")


# Створення екземпляру додатку
app = FastAPI(lifespan=lifespan)

# Додаємо CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Конектимо роут
app.include_router(base_router)

# Обслуговування статичних файлів
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("app.main:app",  reload=settings.reload, host=settings.host, port=settings.port)
