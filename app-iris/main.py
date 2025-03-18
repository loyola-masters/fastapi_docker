import logging
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load the pre-trained model from file
logger.info("Loading the pre-trained Iris model from file: iris_model.joblib")
model = joblib.load("iris_model.joblib")
logger.info("Model loaded successfully")

# Map numeric classes to Iris species names
iris_species = ["setosa", "versicolor", "virginica"]

# Create the FastAPI application
app = FastAPI()

# Pydantic model for the Iris features
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict_iris(data: IrisInput):
    """
    Predict the Iris species given measurements.
    """
    features = np.array([[data.sepal_length, data.sepal_width,
                          data.petal_length, data.petal_width]])
    
    logger.info(f"Received prediction request: {features.tolist()}")
    prediction = model.predict(features)[0]
    predicted_species = iris_species[prediction]
    logger.info(f"Returning prediction: {predicted_species} (class {prediction})")
    
    return {
        "prediction": int(prediction),
        "predicted_species": predicted_species
    }

@app.get("/")
def root():
    return {"message": "Hello, I'm serving a saved Iris model with FastAPI!"}
