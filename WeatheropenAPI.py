import requests
import math
import time 
import datetime
import json

#This will be how the system gathers weather data, i haven't read into the GUI much, so into the terminal it goes
#Just grab zipcode first
def Latlon(zpcode):
    print("Zipcode: " +zpcode) #Why in the everloving EARTH do I have to define it like this first.

    Location = f"https://nominatim.openstreetmap.org/search?q={zpcode}&format=json" #fstrings are really neat
    response = requests.get(Location)
    data = response.json()#Reading the JSON
    lat = data[0]['lat'] #grabbing ze data
    lon = data[0]['lon']
    return lat, lon

#Now for the weather, maybe eventually
def weathergrab(lat, lon, set):
    #bazinga
    weather = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,alerts,minutely&appid=dbfe113373f8e233af2191ce8daf6a90"
   #call complete ring ring ring
    response = requests.get(weather)
    data = response.json()
    date1 = data['daily'][set]['dt']
    readdate1 = datetime.datetime.fromtimestamp(date1).strftime('%d-%m-%Y')
    low1 = data['daily'][set]['temp']['min']
    high1 = data['daily'][set]['temp']['max'] #I think this is right?
    #descrip = data['daily'][0]['weather']['0']  This was being fickle, it's not use to a string i suppose
    return readdate1, low1, high1
    

zipcode = input("Input your zipcode: " ) #I didn't know you could shorthand this

lat, lon = Latlon(zipcode)

print(f"Lat: {lat}, Lon: {lon}")

date1, low1, high1 = weathergrab(lat, lon, 0) #Today's weather, date of today, high and low
date2, low2, high2 = weathergrab(lat, lon, 1) #Tomorrow's weather, date of course, high and low
date3, low3, high3 = weathergrab(lat, lon, 2) #The day after tomorrow, ditto as above

print(f"Date: {date1}, Low: {low1} High: {high1}")

print(f"Date: {date2}, Low: {low2} High: {high2}")
print(f"Date: {date3}, Low: {low3} High: {high3}")
#This currently works to display temps, and date in command line, getting it into PyQt
#is going to be the fun bit