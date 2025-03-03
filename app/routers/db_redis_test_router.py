from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db import get_db
from app.db.redis import get_redis

db_redis_test_router = APIRouter()

@db_redis_test_router.get("/db_redis_test")
async def db_redis_test_route(
    db: AsyncSession = Depends(get_db),
    redis=Depends(get_redis)
):
    await redis.set("test_key", "value")
    value = await redis.get("test_key")
    return {"redis_test": value}