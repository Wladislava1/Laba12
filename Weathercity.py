from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/weather/{city_id}")
def get_weather(city_id: int):
    api_key = "YOUR_API_KEY"

    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200:

        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        return {
        "temperature": temperature,
        "humidity": humidity,
        "description": description
    }
    else:
        return {"error": "Failed to retrieve weather data"}
