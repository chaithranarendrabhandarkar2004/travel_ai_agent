def calculate_budget(flight_price, hotel_price, days):

    food_and_transport_per_day = 2500

    total = (
        flight_price +
        ((hotel_price + food_and_transport_per_day) * days)
    )

    return total