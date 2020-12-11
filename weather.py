import requests
import subprocess
import jsonHandler as jR

api_key_weather = ""
base_url_weather = "http://api.openweathermap.org/data/2.5/weather?"

api_key_ip = ""
base_url_ip = "http://ipinfo.io/"




# complete_url_ip = base_url_ip + ipAddress + "?token=" + api_key_ip
'''
response = requests.get(complete_url_ip)
x = response.json()
if x["status"] == 403:
    print("enter a valid token")
elif x["status"] == 404:
    print("enter a valid")
'''
# complete_url_weather = base_url_weather + "appid=" + api_key_weather + "&q=" + city_name


# print(ipAddress)
'''
response = requests.get(complete_url_weather)
x = response.json()
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n humidity (in percentage) = " +
          str(current_humidity) +
          "\n description = " +
          str(weather_description))
else:
    print(" City Not Found ")
'''

