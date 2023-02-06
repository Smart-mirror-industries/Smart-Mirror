import requests
import math
import time 

#This will be how the system gathers weather data, i haven't read into the GUI much, so into the terminal it goes
day1
day2
day3
#Just grab zipcode first
def Latlon(zpcode):
    print("Zipcode: " +zpcode) #Why in the everloving EARTH do I have to define it like this first.

    Location = f"https://nominatim.openstreetmap.org/search?q={zpcode}&format=json"
    response = requests.get(Location)
    data = response.json()#Reading the JSON
    lat = data[0]['lat'] #grabbing ze data
    lon = data[0]['lon']
    return lat, lon

#Now for the weather, maybe eventually
def weathergrab(lat, lon):
    #bazinga
    weather= f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,alerts,minutely&appid=dbfe113373f8e233af2191ce8daf6a90"
   #call
    response = requests.get(weather)
    data = weather.josn()


    return
    

zipcode = input("Input your zipcode: " ) #I didn't know you could shorthand this

lat, lon = Latlon(zipcode)

print(f"Lat: {lat}, Lon: {lon}")

weathergrab(lat, lon)
