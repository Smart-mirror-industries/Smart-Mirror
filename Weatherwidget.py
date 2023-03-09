import requests
import datetime
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

class weatherwidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(450, 150) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) #if the MinSize is too big, the text position will not match the move command
                                                        #because it will be centering the text to the middle of the large label

        # makes a timer to update the time every second
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.Showreport) #connects the timer to the showTime def (function)
        self.timer.start(43200000) # 43200000 = 12 hours
        self.Showreport() # runs showTime initially to get rid of delay at program start

    # function that "re-draws" the widget so it displays every 12 hours
    def Showreport(self):
        zipcode = 32931
        
        lat, lon = self.getLocation(zipcode) #Just so that it does it ONCE, and not again
        
        date1, low1, high1, descrip1 = self.getReport(lat, lon, 0)
        text = (f"Date: {date1} \nLow: {low1} \nHigh: {high1}\n Description: {descrip1}\n")
        self.setText(text)

        # TODO: make it grab the following days, and report back.  This needs to not exceed some limit with the api so I can't test.
        
    
    def getReport(self, lat, lon, set): # get report
        #initilzaize report
        
        weather = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,alerts,minutely&appid=dbfe113373f8e233af2191ce8daf6a90"
   
        response = requests.get(weather)
        data = response.json()
        date1 = data['daily'][set]['dt']
        readdate1 = datetime.datetime.fromtimestamp(date1).strftime('%d-%m-%Y')
        low1 = data['daily'][set]['temp']['min']
        high1 = data['daily'][set]['temp']['max'] 
        descrip = data['daily'][set]['weather'][0]['main']  #found the issue, '0' around that one 0 is what was doing it.  Making it think it was an integer
        return readdate1, low1, high1, descrip
        pass
   
    def getLocation(self, zpcode):
        # get location, could could be copied from there
        #print("Zipcode: " +zpcode) 

        Location = f"https://nominatim.openstreetmap.org/search?q={zpcode}&format=json" #hopefully I don't abuse Nominatim
        response = requests.get(Location)
        data = response.json()#Reading the JSON
        lat = data[0]['lat'] #This should work just shoehorned in yeah?
        lon = data[0]['lon']
        return lat, lon
        
