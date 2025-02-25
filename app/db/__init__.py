import json
import os
from fastapi.exceptions import HTTPException
from app.config import settings

# Шлях до JSON-файлу
DATA_PATH = settings.data_file

def load_message():
    try:
        # Перевірка існування файлу
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"File {DATA_PATH} not found")
        
        # Читання файлу
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Перевірка структури даних
        if "status_code" not in data:
            raise ValueError("Invalid JSON structure: 'status_code' key missing")

        if "detail" not in data:
            raise ValueError("Invalid JSON structure: 'detail' key missing")
        
        if "result" not in data:
            raise ValueError("Invalid JSON structure: 'result' key missing")
        
        return data
        
    except Exception as e:
        # Логування помилки
        print(f"Error loading message: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to load data"
        )