from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer, Qt
from Calendar import Ui_Form

import requests
from ics import Calendar, Event
import pandas as pd

import settings
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
        self.setMouseTracking(True)

        self.move(800,800)
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.getCalendarEvents) #connects the timer to the showTime def (function)
        self.timer.start(1000) # update every 8 ms = 120Hz
        #self.getCalendarEvents() # runs showTime initially to get rid of delay at program start

        self.timer2 = QTimer(self) # makes a timer
        self.timer2.timeout.connect(self.updateTheme) #connects the timer to the showTime def (function)
        self.timer2.start(1000) # update every 8 ms = 120Hz
        self.updateTheme() # runs showTime initially to get rid of delay at program start

    def updateTheme(self):
        self.ui.calendarWidget.setStyleSheet("font: 15pt Arial; color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        # self.label.setStyleSheet("font: 25pt Arial: color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))

    def addLabel(self):
        self.label = QLabel(self)
        self.label.setText('test')
        self.setStyleSheet("color: {};".format(settings.colorthemetext))

        self.label.setStyleSheet("font: 15pt Arial; color: {}; background-color: rgba(255, 255, 255, 0);".format(settings.colorthemetext))

    def getCalendarEvents(self):
        
        events = "none"
        if self.getDate() in calendarDates:
            events = (calendarDates[self.getDate()])
        #except: 
        #    print("error")
        self.label.setText(events[0])
        

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
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag_distance = event.pos() - self.drag_start_position
            self.move(self.x() + drag_distance.x(), self.y() + drag_distance.y())