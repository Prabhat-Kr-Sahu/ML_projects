FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    clang \
    make \
    build-essential \
    python3-dev \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*  # Cleanup to reduce image size

# Copy application files
COPY . /app
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use JSON CMD format
CMD ["python", "app.py"]
