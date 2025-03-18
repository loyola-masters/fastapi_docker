# Use a lightweight Python base image
FROM python:3.9-slim

# Create a working directory
WORKDIR /fastapi

# Copy requirements and install them
COPY requirements.txt /fastapi/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /fastapi

# 1) Run the training script to generate 'iris_model.joblib'
RUN python train_model.py

# Expose port 80
EXPOSE 80

# 2) Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
