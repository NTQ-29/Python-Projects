import requests

MY_API_KEY = "********"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Please enter a city name: ")
url_request = f"{BASE_URL}?appid={MY_API_KEY}&q={city}"
response = requests.get(url_request)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    print(weather)
    temp = round(data["main"]["temp"]-273.5, 2)
    print(f"Temperature: {temp:.2f}ºF")

else:
    print(f"Error {response.status_code}: Couldn't retrieve weather details for '{city}'")
#Error 401: Couldn't retrieve weather details for 'Leesburg' | need to wait 2 hrs
#after creating openweathermap account, there's a lag in API calls after retrieving key
