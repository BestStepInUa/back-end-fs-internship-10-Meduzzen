# FS Internship 10 | Meduzzen Back-end part by Oleksandr Vasylenko

1. To create a Virtual Environment use: uv venv

2. To activate the Virtual Environment use: source .venv/bin/activate

3. If you want to take part in my project like new contibutor, you should install dev libraries, use: uv sync

4. For production use: uv sync --no-dev

5. To start dev use: python -m app.main

6. To start tests use: pytest -v

To launch the application within Docker:

1. Create (update) the uv.lock file, which contains the exact versions of all dependencies: uv lock

2. Assemble the image: docker build -t fastapi-app .

3. Run the container: docker run -d -p 8000:8000 --name my_fastapi fastapi-app
