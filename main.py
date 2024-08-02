import requests as r

api_key = "65bed5c069ccfb53c44648160e7bc41b"
response = r.get("https://api.openweathermap.org/data/2.5/weather", params={"q":"Oldham,UK", "appid": api_key})
response.raise_for_status()

print(response.status_code)
print(response.content)

print("---------------------------")
print(response.json()["weather"])
print()