import random

# Predefined weather conditions
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Windy", "Foggy"]
cities = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru", "Malindi", "Garissa"]

def get_weather(city):
    """Generates random weather data for a city."""
    if city not in cities:
        return f"Weather data for {city} is not available."
    
    weather_info = {
        "City": city,
        "Temperature": f"{random.randint(15, 35)}°C",
        "Humidity": f"{random.randint(30, 90)}%",
        "Weather": random.choice(weather_conditions),
        "Wind Speed": f"{random.uniform(1.0, 10.0):.1f} m/s"
    }
    return weather_info

if __name__ == "__main__":
    city_name = input("Enter city name: ").title()
    weather_details = get_weather(city_name)
    
    if isinstance(weather_details, dict):
        print("\nWeather Information:")
        for key, value in weather_details.items():
            print(f"{key}: {value}")
    else:
        print(weather_details)
