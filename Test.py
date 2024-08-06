import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def get_weather():
    url = "https://api.weather.gov/gridpoints/DLH/140,132/forecast"
    weather_headers = {
        "User-Agent": "sandrambo11@live.com",
        "Accept": "application/Id+json"
    }

    response = requests.get(url, headers=weather_headers)
    print(response.status_code)

    # Latitude and longitude of Norse Hus
    latitude = 47.7613
    longitude = -90.3434

    # NWS API endpoint
    points_url = f"https://api.weather.gov/points/{latitude},{longitude}"

    # Fetch location information
    response = requests.get(points_url)
    data = response.json()

    # Extract observation station URL
    observation_stations_url = data['properties']['observationStations']

    # Fetch observation station data
    stations_response = requests.get(observation_stations_url)
    stations_data = stations_response.json()
    stations = stations_data['observationStations']

    # Fetch data from the first observation station
    station_url = stations[0]

    # Fetch current weather data
    current_weather_url = f"{station_url}/observations/latest"
    current_weather_response = requests.get(current_weather_url)
    current_weather_data = current_weather_response.json()

    # Print current weather information
    current_observation = current_weather_data['properties']

    # print("Current Weather")
    # print(f"Temperature: {current_observation['temperature']['value']}°C")
    # print(f"Humidity: {current_observation['relativeHumidity']['value']}%")
    # print(f"Wind Speed: {current_observation['windSpeed']['value']} m/s")
    # print(f"Wind Direction: {current_observation['windDirection']['value']}°")
    # print(f"Weather Description: {current_observation['textDescription']}")

    temp_output = current_observation['temperature']['value']
    humidity_output = round(current_observation['relativeHumidity']['value'], 0)
    wind_speed_current = current_observation['windSpeed']['value']
    wind_dir_current = current_observation['windDirection']['value']
    description_current = current_observation['textDescription']

    return render_template("index.html",
                           temp=temp_output,
                           humidity=humidity_output,
                           windSpeed=wind_speed_current,
                           windDir=wind_dir_current,
                           description=description_current)


if __name__ == "__main__":
    app.run(debug=True)
