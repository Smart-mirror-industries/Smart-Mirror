# import pyqt6 stuff
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QMouseEvent
import settings


# import custom subclasses
from timewidget import TimeWidget
from stockscroller import StockScroller
from Weatherwidget import weatherwidget
from MapWidget import MapWidget
from ThemeWidget import ThemeWidget
from CalendarWidget import CalendarWidget
from ScreenClutterWidget import ScreenClutterWidget
from Reminderwidget import reminderwidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setStyleSheet("background-color: {};".format(settings.mainwindowcolor))

        self.showhideThemesButton = QPushButton('Toggle Theme Selector', self)
        self.showhideThemesButton.setStyleSheet("font: 15pt Arial; color: white; background-color: black")
        self.showhideThemesButton.setGeometry(1300, 820, 225, 50)
        self.showhideThemesButton.clicked.connect(self.toggle_ThemeSelector)

        self.screenclutter_widget = ScreenClutterWidget(self)
        self.screenclutter_widget.move(1100,650)
        self.screenclutter_widget.setMinimumSize(200,300)

        self.theme_widget = ThemeWidget(self)
        self.theme_widget.move(1300,620)
        self.theme_widget.setMinimumSize(200, 200)

        self.time_widget = TimeWidget(self)
        self.time_widget.move(450, 100)

        self.stock_scroller = StockScroller(self)
        self.stock_scroller.setMinimumSize(3000, 50)

        self.weather_widget = weatherwidget(self)
        self.weather_widget.move(75,200)
        
        self.stock_scroller.move(-200, 50)


        self.map_widget = MapWidget(self)
        self.map_widget.move(800,50)
        self.map_widget.setMinimumSize(500, 500)


        self.reminderwidget = reminderwidget(self)
        self.reminderwidget.move(75,200)
        self.reminderwidget.setMinimumSize(200,200)

        self.calendar_widget = CalendarWidget(self)
        self.calendar_widget.move(500,500)
        self.calendar_widget.setMinimumSize(500, 300)

        # makes a timer to refresh the mainwindow screen with updates
        self.updateMainWindowColorAndThemeButtonColortimer = QTimer(self) # makes a timer
        self.updateMainWindowColorAndThemeButtonColortimer.timeout.connect(self.screenRefresh) #connects the timer to the screenRefresh def (function)
        self.updateMainWindowColorAndThemeButtonColortimer.start(1000) # 1000ms = 1 second
        self.screenRefresh() # runs screenRefresh initially to get rid of delay at program start


    def toggle_ThemeSelector(self):
        if settings.themewindowswitcher == 1:
            self.theme_widget.hide()
            self.screenclutter_widget.hide()
            settings.themewindowswitcher = 0
        elif settings.themewindowswitcher == 0:
            self.theme_widget.show()
            self.screenclutter_widget.show()
            settings.themewindowswitcher = 1

    def screenRefresh(self):
        self.setStyleSheet("background-color: {};".format(settings.mainwindowcolor))
        self.showhideThemesButton.setStyleSheet("font: 15pt Arial;color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        if settings.timewidgetVisibility == 1:
            self.time_widget.show()
        else: self.time_widget.hide()
        if settings.weatherwidgetVisibility == 1:
            self.weather_widget.show()
        else: self.weather_widget.hide()
        if settings.stockwidgetVisibility == 1:
            self.stock_scroller.show()
        else: self.stock_scroller.hide()
        if settings.mapwidgetVisibility == 1:
            self.map_widget.show()
        else: self.map_widget.hide()
        # if settings.calenderwidgetVisibility == 1:
        #     self.calenderwidgetVisibility.show()
        # else: self.calenderwidgetVisibility.hide()

        

    def toggle_ThemeSelector(self):
        if settings.themewindowswitcher == 1:
            self.theme_widget.hide()
            self.screenclutter_widget.hide()
            settings.themewindowswitcher = 0
        elif settings.themewindowswitcher == 0:
            self.theme_widget.show()
            self.screenclutter_widget.show()
            settings.themewindowswitcher = 1

    def screenRefresh(self):
        self.setStyleSheet("background-color: {};".format(settings.mainwindowcolor))
        self.showhideThemesButton.setStyleSheet("font: 15pt Arial;color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        if settings.timewidgetVisibility == 1:
            self.time_widget.show()
        else: self.time_widget.hide()
        if settings.weatherwidgetVisibility == 1:
            self.weather_widget.show()
        else: self.weather_widget.hide()
        if settings.stockwidgetVisibility == 1:
            self.stock_scroller.show()
        else: self.stock_scroller.hide()
        if settings.mapwidgetVisibility == 1:
            self.map_widget.show()
        else: self.map_widget.hide()
        # if settings.calenderwidgetVisibility == 1:
        #     self.calenderwidgetVisibility.show()
        # else: self.calenderwidgetVisibility.hide()

        

