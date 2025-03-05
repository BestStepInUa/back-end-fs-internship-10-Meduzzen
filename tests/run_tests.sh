#!/bin/bash
set -e

# Видаляємо файл тільки якщо він існує
[ -f "/temp/tests_exe" ] && rm /temp/tests_exe || true

# Запуск тестів через Python модуль
python -m pytest --maxfail=1 --disable-warnings tests/

if [ $? -eq 0 ]; then
  touch /temp/tests_exe
  echo "Tests passed. Starting FastAPI..."
else
  echo "Tests failed. Stopping all containers..."
  exit 1
fi