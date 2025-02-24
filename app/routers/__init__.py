from fastapi import APIRouter
from app.db import load_message
from fastapi.exceptions import HTTPException

#Простий GET-ендпоїнт для тестування
base_router = APIRouter()

@base_router.get("/")
async def read_root():
    try:
        data = load_message()
        return data
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )