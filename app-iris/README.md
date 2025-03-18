## Train the mode
This generates the output file `iris_model.joblib` that will be used by the API to serve predictions:
```python
python train_model.py
```

## Building and Running

1. **Build** the Docker image:
   ```bash
   docker build -t fastapi-iris .
   ```
2. **Run** a container from that image:
   ```bash
   docker run -d -p 8001:80 --name fastapi-iris-app fastapi-iris
   ```
3. Test at [http://127.0.0.1:8001](http://127.0.0.1:8001).

Use the above commands on your system where Docker is installed and configured.

(This is done by Docker) Run the FastAPI server (e.g., `uvicorn main:app --reload`) and then send a POST request to `/predict` with the Iris flower measurements to get a prediction.

## How to test the Iris prediction endpoint

1. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
2. Send a POST request to `http://127.0.0.1:8001/predict` with JSON body, for example:
   ```json
   {
     "sepal_length": 5.1,
     "sepal_width": 3.5,
     "petal_length": 1.4,
     "petal_width": 0.2
   }
   ```
   You can test this via [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs) in your browser or with a tool like `curl` or Postman. The response will look like:
   ```json
   {
     "prediction": 0,
     "predicted_species": "setosa"
   }
   ```

   **Using Powershell**
```powershell
   Invoke-RestMethod `
  -Uri http://127.0.0.1:8001/predict `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

# ANNEX: Dockerfile explained
Below is an example **Dockerfile** adapted to run your FastAPI Iris app. It closely follows your original template but includes a few best practices and minor adjustments (such as using a more recent Python base image, adding `EXPOSE`, and avoiding cached dependencies). Adjust paths and filenames to match your own project structure:

```dockerfile
# Use a more recent Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /fastapi

# Copy requirements and install them
COPY requirements.txt /fastapi/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /fastapi

# Expose port 80 to the outside world
EXPOSE 80

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

### Key points:
1. **FROM python:3.9-slim**: Uses a slim Python 3.9 image (lighter than a full Python image).
2. **WORKDIR /fastapi**: Establishes `/fastapi` as the working directory inside the container.
3. **COPY requirements.txt /fastapi/requirements.txt** + **RUN pip install**: Copies and installs dependencies without caching to reduce image size.
4. **COPY . /fastapi**: Copies your application files (including `main.py`, `app/`, etc.) into the container.
5. **EXPOSE 80**: Not strictly required, but a good convention. This signals that the container listens on port 80.
6. **CMD**: Calls **uvicorn** to serve `app.main:app`. Make sure this matches the Python module path to your FastAPI object. 

If you placed your FastAPI code (the one containing `app = FastAPI()`) in `app/main.py`, then `app.main:app` is correct. If your structure is different, adjust accordingly (for example, `main:app` if the file is at the project root).