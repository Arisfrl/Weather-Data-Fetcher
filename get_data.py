import requests

# Read from api_key
file1 = open('api_key.txt', 'r')
Line = file1.readline()

city = "Kolkata"
apikey = Line
baseurl = "https://api.openweathermap.org/data/2.5/weather"

res = requests.get(f'{baseurl}?q={city}&appid={apikey}&units=metric')
if res.status_code == 200:
    print("Weather data for", city, "is:")
    print (res.json())
    for key in res.json().keys():
        print(key, ":", res.json()[key])

