import joblib
import numpy as np
import os

# Determine the base directory path relative to this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "model.pkl")

# Load the pre-trained machine learning model from disk
model = joblib.load(MODEL_PATH)

def predict_risk(data):
    """
    Generates disease risk prediction based on environmental parameters.
    Important: Feature order must match the training data sequence exactly.
    """
    # Construct feature array maintaining the same column order as during training
    features = np.array([[
        data.temperature,
        data.humidity,
        data.rainfall,
        data.soil_pH
    ]])

    # Generate prediction using the loaded model
    prediction = model.predict(features)[0]

    # Convert binary prediction to human-readable risk level
    return "High" if prediction == 1 else "Low"
