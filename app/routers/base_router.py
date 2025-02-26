from fastapi import APIRouter, status

base_router = APIRouter()

#Simple GET endpoint for testing
@base_router.get("/")
async def read_root():
    return {
        "status_code": status.HTTP_200_OK,
        "detail": "ok",
        "result": "working"
        }