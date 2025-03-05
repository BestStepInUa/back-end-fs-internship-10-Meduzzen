import redis.asyncio as redis

from app.config import settings

async def get_redis():
    connection = redis.from_url(settings.redis_url)
    try:
        yield connection
    finally:
        await connection.close()