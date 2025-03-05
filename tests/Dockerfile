# Use the official Python image
FROM python:3.12-slim

# Set up the working directory
WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy the configuration files
COPY pyproject.toml uv.lock ./
COPY pytest.ini ./

# Install dependencies via uv from pyproject.toml
RUN uv sync

# Copy the project files
COPY . .

# Add rights to execute scripts
COPY tests/run_tests.sh /run_tests.sh
RUN chmod +x /run_tests.sh

ENV PYTHONUNBUFFERED=1

# Run the tests
ENTRYPOINT ["/run_tests.sh"]