import redis.asyncio as redis
from contextlib import asynccontextmanager

REDIS_URL = "redis://redis:6379/0"

@asynccontextmanager
async def get_redis():
    connection = redis.from_url(REDIS_URL)
    try:
        yield connection
    finally:
        await connection.close()