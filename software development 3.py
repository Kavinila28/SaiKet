import requests

API_KEY = "05e9648a9030a95858bcc4a85691ad4b"
CITY = "Chennai"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"\n📍 City: {CITY}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"⛅ Weather: {weather.title()}")
else:
    print(f"❌ Error: Status Code {response.status_code}")
    print("Message:", response.text)
