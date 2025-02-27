# FS Internship 10 | Meduzzen Back-end part by Oleksandr Vasylenko

1. To create a Virtual Environment use: uv venv

2. To activate the Virtual Environment use: source .venv/Scripts/activate

3. Change to installing dependencies with the command: uv add "fastapi[all]" (or use: uv pip install "fastapi[all]")

4. Change to installing dependencies with the command: uv add httpx pytest --dev

5. To start dev use: python -m app.main

6. To start tests use: pytest -v

To launch the application within Docker:

1. Create (update) the uv.lock file, which contains the exact versions of all dependencies: uv lock

2. Assemble the image: docker build -t fastapi-app .

3. Run the container: docker run -d -p 8000:8000 --name my_fastapi fastapi-app
