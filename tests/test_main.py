import pytest
from fastapi.testclient import TestClient
from app.main import app

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