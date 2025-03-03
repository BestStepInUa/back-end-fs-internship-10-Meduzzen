import pytest
from fastapi.testclient import TestClient
from app.db.redis import get_redis
from app.main import app
import redis.asyncio as redis
from redis.exceptions import ConnectionError

# Successful case test
def test_read_root_success():
    client = TestClient(app)
    response = client.get("/")
        
    # Check status code and response content
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
        }
    
# Фікстура для асинхронного Redis клієнта
@pytest.fixture(scope="module")
async def redis_client():
    # Створюємо підключення
    client = redis.Redis.from_url("redis://localhost:6379/0")
    yield client  # Повертаємо об'єкт клієнта
    await client.close()  # Закриваємо з'єднання

# Асинхронний тест для Redis
@pytest.mark.asyncio
async def test_redis_connection(redis_client):
    try:
        # Перевірка підключення
        assert await redis_client.ping() is True
        
        # Тест запису/читання даних
        await redis_client.set("test_key", "value")
        value = await redis_client.get("test_key")
        assert value == b"value"
    except ConnectionError:
        pytest.fail("Помилка підключення до Redis")    