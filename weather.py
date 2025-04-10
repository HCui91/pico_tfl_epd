# Python
"""A very simple wrapper for the OpenWeather API.

This module provides a simple wrapper for the OpenWeather API. It allows for
testing the connection to the API, fetching weather status, and temperature.
"""

import urequests
import ujson
import time
import gc

def parse_weather_endpoint(api_key: str, lat: float, lon: float) -> str:
    """
    Parse the endpoint URL for the OpenWeather API.
    """
    return f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

def test_weather_connection(weather_endpoint: str) -> bool | int:
    """
    Test connectivity to the OpenWeather API.
    """
    response = None
    try:
        response = urequests.get(weather_endpoint)
        return True if response.status_code == 200 else response.status_code
    except Exception as e:
        return False
    finally:
        if response:
            response.close()
        gc.collect()

def fetch_weather(weather_endpoint: str) -> tuple[str, str]:
    """
    Fetch and return current weather description and temperature from the API.
    """
    response = None
    try:
        response = urequests.get(weather_endpoint)
        data = response.json()
        weather = data.get("weather", [{}])[0].get("description", "Parsing error")
        temperature = int(data.get("main", {}).get("temp", -999))
        if temperature == -999:
            return weather, "--*C"
        return weather, f"{temperature}*C"
    except Exception as e:
        return "Fetch error", "--*C"
    finally:
        if response:
            response.close()
        gc.collect()