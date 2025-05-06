# Use a base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements (if you have any)
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Command to run when container starts
CMD ["python", "dummy.py"]