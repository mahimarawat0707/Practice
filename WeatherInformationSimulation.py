weather_data = {
    "Chandigarh": {"temp": 26, "condition": "Sunny"},
    "Delhi": {"temp": 31, "condition": "Cloudy"},
    "Mumbai": {"temp": 29, "condition": "Rainy"},
}

def get_weather(city):
    return weather_data.get(city, "❌ No data available for that city.")

city = input("Enter city: ")
print(get_weather(city))
