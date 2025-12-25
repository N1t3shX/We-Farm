import random

def get_ndvi(latitude: float, longitude: float):
    """
    Generates a mock Normalized Difference Vegetation Index value for the specified geographic coordinates.
    This is a temporary implementation that produces synthetic data. Future iterations will integrate
    actual satellite imagery APIs to retrieve real-time vegetation indices.
    """

    # Generate vegetation index values within typical observed ranges
    ndvi = round(random.uniform(0.2, 0.85), 2)

    # Classify vegetation condition based on NDVI thresholds
    if ndvi > 0.6:
        health = "Healthy vegetation"
    elif ndvi > 0.4:
        health = "Moderate stress"
    else:
        health = "Severe stress"

    return {
        "ndvi": ndvi,
        "vegetation_health": health
    }
