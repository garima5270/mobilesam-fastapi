# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Git
RUN apt-get update && apt-get install -y git

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libglib2.0-dev \
    && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py tools.py mobile_sam.pt app.py requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your FastAPI service using uvicorn
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"]
