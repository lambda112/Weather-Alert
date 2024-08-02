import requests as r

# Get Information From Website
api_key = "65bed5c069ccfb53c44648160e7bc41b"
response = r.get("https://api.openweathermap.org/data/2.5/forecast", params={"lat":53.537980, "lon":-2.092610, "appid": api_key, "cnt":7})
response.raise_for_status()

# Turn to json
weather_data = response.json()["list"]
weather_dict = {}

for index, data in enumerate(weather_data):
    weather_dict[index] = data

def find_weather(time: int) -> list:
    time = time // 3
    return weather_dict[time]

for key, val in weather_dict.items():
    info = val["weather"][0]
    time = val["dt_txt"]
    code = info["id"]
    weather = info["main"]
    detailed_weather = info["description"]
    is_umbrella = "Bring an Umbrella!" if code < 700 else "Dont Need Umbrella!"

    print(f"{time=}, {code=}, {weather=}, {detailed_weather=}, {is_umbrella}")