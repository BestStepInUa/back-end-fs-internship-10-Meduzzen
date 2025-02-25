import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

# Тест для успішного випадку
def test_read_root_success():
    # Mock шляху до JSON з даними
    with patch("app.db.DATA_PATH", "app/db/test.data.json"):
        client = TestClient(app)
        response = client.get("/")
        
        # Перевірка статус-коду та вмісту відповіді
        assert response.status_code == 200
        assert response.json() == {
            "status_code": 200,
            "detail": "ok",
            "result": "working"
        }

# Тест для випадку, коли файл не знайдено
def test_read_root_file_not_found():
    with patch("app.db.DATA_PATH", "notValidData.json"):
        client = TestClient(app)
        response = client.get("/")
        
        assert response.status_code == 500
        assert response.json()["detail"] == "Failed to load data"

# Тест для невалідної структури JSON
def test_read_root_invalid_structure(tmpdir):
    import json
    # Створюємо тимчасовий файл з невірною структурою
    invalid_data = {"wrong_key": "value"}
    temp_file = tmpdir.join("temp.json")
    temp_file.write(json.dumps(invalid_data))
    
    with patch("app.db.DATA_PATH", str(temp_file)):
        client = TestClient(app)
        response = client.get("/")
        
        assert response.status_code == 500
        assert "Failed to load data" in response.json()["detail"]