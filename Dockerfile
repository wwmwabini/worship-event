# Use official Python Alpine image for minimal size
FROM python:3.12-alpine

# Set working directory
WORKDIR /app/core

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    linux-headers \
    pkgconfig \
    && rm -rf /var/cache/apk/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY core .

# Collect static files
RUN python manage.py collectstatic --noinput

# Create directory for media files
RUN mkdir -p /app/media

# Expose port 8000
EXPOSE 8000

# Run uvicorn
CMD ["/bin/sh", "-c", "cd core; uvicorn core.core.asgi:application --host 0.0.0.0 --port 8000"]
