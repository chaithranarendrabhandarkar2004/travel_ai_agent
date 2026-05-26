import json


def search_places(city):

    with open("data/places.json", "r") as file:
        places = json.load(file)

    results = [
        place for place in places
        if place["city"].lower() == city.lower()
    ]

    return results[:5]