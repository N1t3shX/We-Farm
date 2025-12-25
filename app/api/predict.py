from fastapi import APIRouter
from pydantic import BaseModel
from app.services.weather import get_weather
from app.services.satellite import get_ndvi
from app.services.disease_model import predict_disease

router = APIRouter()

class PredictRequest(BaseModel):
    """
    Request model for crop disease prediction endpoint.
    Contains crop type, observed symptoms, and geographic coordinates.
    """
    crop: str
    symptoms: str
    latitude: float
    longitude: float

@router.post("/predict")
def predict(data: PredictRequest):
    """
    Main prediction endpoint that aggregates weather data, satellite imagery,
    and symptom analysis to provide comprehensive crop disease assessment.
    """
    current_weather = get_weather(data.latitude, data.longitude)
    vegetation_index = get_ndvi(data.latitude, data.longitude)

    disease_analysis = predict_disease(
        data.crop,
        data.symptoms,
        current_weather
    )

    return {
        "crop": data.crop,
        "symptoms": data.symptoms,
        "weather": current_weather,
        "satellite": vegetation_index,
        "prediction": disease_analysis["disease"],
        "risk": disease_analysis["risk"],
        "confidence": disease_analysis["confidence"],
    }
