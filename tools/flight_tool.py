import json


def search_flights(source, destination):

    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    results = [
        flight for flight in flights
        if flight["source"].lower() == source.lower()
        and flight["destination"].lower() == destination.lower()
    ]

    if not results:
        return None

    cheapest = min(results, key=lambda x: x["price"])

    return cheapest