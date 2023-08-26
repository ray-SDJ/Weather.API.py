import requests

API_KEY ="1ca2d2cc276617dbb5b6eba133770880"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f" The Weather is {weather} and the temperature is {temperature} degree celcius")
else:
    print("Error")
    
    
while city is not None:
    city = input("Enter the city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)
        print(f" The Weather is {weather} and the temperature is {temperature} degree celcius")
    else:
        print("Error")