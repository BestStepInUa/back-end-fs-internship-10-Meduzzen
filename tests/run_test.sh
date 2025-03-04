#!/bin/bash

rm /temp/tests_exe

pytest --maxfail=1 --disable-warnings

if [ $? -eq 0 ]; then
  touch /temp/tests_exe
  echo "Tests passed. Starting FastAPI..."
else
  echo "Tests failed. Stopping all containers..."
  exit 1
fi