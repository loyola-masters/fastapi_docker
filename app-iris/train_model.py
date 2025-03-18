import logging
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -------------------------------------------------------------------
# 1. Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# 2. Load the Iris dataset
logger.info("Loading the Iris dataset.")
iris = load_iris()
X, y = iris.data, iris.target
logger.info(f"Dataset loaded. Feature shape: {X.shape}, Target shape: {y.shape}")

# -------------------------------------------------------------------
# 3. Train-test split
logger.info("Splitting the dataset into train and test sets.")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
logger.info(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# -------------------------------------------------------------------
# 4. Train the model
logger.info("Initializing and training the RandomForestClassifier.")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
logger.info("Model training complete.")

# -------------------------------------------------------------------
# 5. Evaluate the model and log metrics
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)
logger.info(f"Training Accuracy: {train_acc:.4f}")
logger.info(f"Test Accuracy: {test_acc:.4f}")

# -------------------------------------------------------------------
# 6. Make 10 predictions on the test set
logger.info("Making 10 predictions on the test set.")
num_predictions = 10
sample_indices = np.arange(min(num_predictions, len(X_test)))
X_samples = X_test[sample_indices]
y_samples_true = y_test[sample_indices]
y_samples_pred = model.predict(X_samples)

iris_species = iris.target_names

logger.info("Sample Predictions:")
for i in range(num_predictions):
    logger.info(
        f"Sample {i+1}: "
        f"Predicted = {iris_species[y_samples_pred[i]]} (class {y_samples_pred[i]}), "
        f"Actual = {iris_species[y_samples_true[i]]} (class {y_samples_true[i]})"
    )

# -------------------------------------------------------------------
# 7. Save the trained model to file
joblib.dump(model, "iris_model.joblib")
logger.info("Model saved to iris_model.joblib")
