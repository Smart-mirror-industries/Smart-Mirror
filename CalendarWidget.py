from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer
from Calendar import Ui_Form

import requests
from ics import Calendar, Event
import pandas as pd

class CalendarWidget(QWidget):
    global calendarDates
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent)
        
       # set a background color for the label
        #self.setStyleSheet("font: 25pt Arial; color: white; background-color: rgba(255, 255, 255, 0)")
        # Create an instance of the Ui_Form class
        self.ui = Ui_Form()
        #self.setMinimumSize(250, 700)
        # Call the setupUi() method and pass the current instance of MyForm as an argument
        self.addLabel()
        self.setCalendar()
        #print(calendarDates)
        self.ui.setupUi(self)
        # Create a vertical layout and add the CalendarWidget to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.ui.calendarWidget)
        self.move(800,800)
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.getCalendarEvents) #connects the timer to the showTime def (function)
        self.timer.start(1000) # update every 8 ms = 120Hz
        #self.getCalendarEvents() # runs showTime initially to get rid of delay at program start
    def addLabel(self):
        self.label = QLabel(self)
        self.label.setText('test')
        self.setStyleSheet("color: white;")

        self.label.setStyleSheet("font: 25pt Arial; color: white; background-color: rgba(255, 255, 255, 0)")

    def getCalendarEvents(self):
        
        events = "none"
        if self.getDate() in calendarDates:
            events = (calendarDates[self.getDate()])
        #except: 
        #    print("error")
        self.label.setText(events[1])

    def setCalendar(self):
        global calendarDates
        calendarDates = {}
        url = 'https://erau.instructure.com/feeds/calendars/user_3tuGhpDjBVOJLZ6wPiMKgXWa0vlyU1o6GoAMeycj.ics'

        r = requests.get(url) # Get Calendar File
        c = Calendar(r.text)  # Read calender file 

        #c.events
        # send a HTTP request to the server and save
        # the HTTP response in a response object called r
        
        eventEnd = ''
        for event in c.timeline:
            #print(event.end)
            eventName = str(event.name)
            eventEnd = str(event.end)
            formattedEnd = eventEnd[:eventEnd.find('T')]#+' '+eventEnd[eventEnd.find('T')+1:]

            if not formattedEnd in calendarDates.keys():
                calendarDates[formattedEnd] = []
            
            calendarDates[formattedEnd].append(eventName)
            #print("Event '{}' end {}".format(event.name, ))
        #for date in calendarDates:
         #   print(calendarDates[date])
        #with open("test.ics",'wb') as f:
        
            # Saving received content as a png file in
            # binary format
            # write the contents of the response (r.content)
            # to a new file in binary mode.
        #    f.write(r.content)
        #    print("test")

    def getDate(self):
        #Get current selected date from calendar
        selectedDate = str(self.ui.calendarWidget.selectedDate().getDate())
        
        #Format the date
        formattedDate = selectedDate[1:selectedDate.find(',')] + '-' 

        #Append a 0 if the day do
        if len(selectedDate)!=2:
            formattedDate+= '0'

        formattedDate += selectedDate[selectedDate.find(',')+2:selectedDate.rfind(',')]
        formattedDate += '-' + selectedDate[selectedDate.rfind(',')+2:len(selectedDate)-1]
        #print(formattedDate)
        #print(selectedDate)
        return formattedDate
