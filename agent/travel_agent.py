from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.places_tool import search_places
from tools.weather_tool import get_weather
from tools.budget_tool import calculate_budget

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)


def generate_trip(source, destination, days):

    flight = search_flights(source, destination)

    hotel = search_hotels(destination)

    places = search_places(destination)

    weather = get_weather(destination)

    if not flight:
        return "No flights found."

    if not hotel:
        return "No hotels found."

    total_budget = calculate_budget(
        flight["price"],
        hotel["price"],
        days
    )

    places_text = "\n".join(
        [f"- {place['place']}" for place in places]
    )

    prompt = f"""
    Create a professional travel itinerary.

    Destination: {destination}
    Number of Days: {days}

    Flight:
    {flight}

    Hotel:
    {hotel}

    Tourist Places:
    {places_text}

    Budget:
    ₹{total_budget}

    Weather:
    {weather}

    Create:
    1. Day-wise itinerary
    2. Budget summary
    3. Travel tips
    """

    response = llm.invoke(prompt)

    return response.content