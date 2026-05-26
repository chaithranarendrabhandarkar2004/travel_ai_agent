import json


def search_hotels(city):

    with open("data/hotels.json", "r") as file:
        hotels = json.load(file)

    results = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
    ]

    if not results:
        return None

    best = max(results, key=lambda x: x["rating"])

    return best