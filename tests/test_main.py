import pytest
from fastapi.testclient import TestClient
from app.main import app
import redis.asyncio as redis
from redis.exceptions import ConnectionError

# Тест для кореневого маршруту
def test_read_root_success():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

# Фікстура з правильною обробкою закриття
@pytest.fixture(scope="function")
async def redis_client(event_loop):
    client = redis.Redis.from_url("redis://localhost:6379/0")
    yield client
    await client.aclose()

# Асинхронний тест
@pytest.mark.asyncio
async def test_redis_connection(redis_client):
    try:
        assert await redis_client.ping() is True
        await redis_client.set("test_key", "value")
        value = await redis_client.get("test_key")
        assert value == b"value"
    except ConnectionError as e:
        pytest.fail(f"Помилка підключення: {str(e)}")   