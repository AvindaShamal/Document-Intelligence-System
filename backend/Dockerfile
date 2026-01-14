FROM python:3.11-slim

# Prevent python buffering
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \ 
    libgl1 \ 
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code (backend project) into /app
COPY backend/ .

# Collect static files
# RUN python manage.py collectstatic --noinput