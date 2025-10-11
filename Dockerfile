# 1. Use an official Python base image
FROM python:3.12-slim

# 2. Set environment variables (avoid writing .pyc, force stdout logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory inside the container
WORKDIR /app

# 4. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first (so Docker caches pip install)
COPY requirements.txt /app/

# 6. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy the rest of the project
COPY . /app/

# 8. Default command (runs the app)
CMD ["gunicorn", "educore.wsgi:application", "--bind", "0.0.0.0:8000"]
