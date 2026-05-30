import requests


def get_weather(destination):
    city_coords = {
        "goa": {"lat": 15.2993, "lon": 74.1240},
        "srinagar": {"lat": 34.0837, "lon": 74.7973},
        "jaipur": {"lat": 26.9124, "lon": 75.7873},
        "manali": {"lat": 32.2396, "lon": 77.1887},
        "kerala": {"lat": 9.9312, "lon": 76.2673}
    }

    coords = city_coords.get(destination.lower(), {"lat": 15.2993, "lon": 74.1240})

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={coords['lat']}&longitude={coords['lon']}&daily=temperature_2m_max"
        "&timezone=auto"
    )

    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
