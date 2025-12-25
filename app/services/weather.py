import requests
import os

OPENWEATHER_API_KEY = os.getenv("4117b0db8d3ae6e7567d46461ffc1b40")


def get_weather(latitude: float, longitude: float):
    """
    Retrieves current weather conditions for a specific geographic location using the OpenWeatherMap API.
    Returns temperature, humidity, precipitation, and general weather description.
    """
    api_endpoint = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={latitude}&lon={longitude}"
        f"&appid={"4117b0db8d3ae6e7567d46461ffc1b40"}&units=metric"
    )

    api_response = requests.get(api_endpoint)
    api_response.raise_for_status()
    weather_data = api_response.json()

    return {
        "temperature": weather_data["main"]["temp"],
        "humidity": weather_data["main"]["humidity"],
        "rainfall": weather_data.get("rain", {}).get("1h", 0),
        "weather": weather_data["weather"][0]["description"],
    }
