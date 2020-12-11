import requests

from internetConnection import InternetConnection

city_name = str(input("enter the name of your city: "))
api_key = str(input("enter your open weather map api key: "))

complete_url_weather = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city_name

if InternetConnection.isConnected():
    file = requests.get(complete_url_weather)
    x = file.json()

    if x["cod"] != "404":
        print("h")
    else:
        print("failed to connect")


'''
for word in range(len(array)):
    print(array[word])
'''
