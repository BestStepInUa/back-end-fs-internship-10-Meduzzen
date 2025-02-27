# Use the official Python image
FROM python:3.12-slim

# Set environment variables by default
ENV PORT=8000 \
    HOST=0.0.0.0 \
    RELOAD=True

# Set up the working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy the configuration files
COPY pyproject.toml uv.lock ./

# Install dependencies via uv from pyproject.toml
RUN uv sync --no-dev --frozen

# Copy the project files
COPY . .

# Open the port
EXPOSE ${PORT}

# Command to run an application with parameters from environment variables
CMD [".venv/bin/python", "-m", "app.main"]