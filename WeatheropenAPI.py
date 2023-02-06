import requests

#This will be how the system gathers weather data

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
    return
    

zipcode = input("Input your zipcode:" ) #I didn't know you could shorthand this

lat, lon = Latlon(zipcode)

print(f"Lat: {lat}, Lon: {lon}")

weathergrab(lat, lon)
