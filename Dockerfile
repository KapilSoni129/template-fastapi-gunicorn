# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Upgrade pip before installing anything else
RUN python -m pip install --upgrade pip

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code into container
COPY app ./app

# Expose port
EXPOSE 8000

# Run the app with gunicorn
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]