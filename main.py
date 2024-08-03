import requests as r
import os
from twilio.rest import Client

# Get Information From Website
api_key = "c6ba93a799a5f2fca3a6b1f2e232520b"
response = r.get("https://api.openweathermap.org/data/2.5/forecast", params={"lat":53.537980, "lon":-2.092610, "appid": api_key, "cnt":7})
response.raise_for_status()

# Turn to json
weather_data = response.json()["list"]
weather_dict = {}

for index, data in enumerate(weather_data):
    weather_dict[index] = data

weather_information = []
for key, val in weather_dict.items():
    info = val["weather"][0]
    time = val["dt_txt"]
    code = info["id"]
    weather = info["main"]
    detailed_weather = info["description"]
    is_umbrella = "Bring an Umbrella!" if int(code) < 700 else "Dont Need Umbrella!"

    weather_information.append(f"{time=}, {code=}, {weather=}, {detailed_weather=}, {is_umbrella}")

message_content = "\n\n".join(weather_information)
account_sid = "AC02e03f4957ae0746b325950da2aad98c"
auth_token = "925f0ac139caa08c93fad7bbf3c6243a"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=message_content,
    from_="whatsapp:+14155238886",
    to="whatsapp:+447547273613",
)

print(message.status)