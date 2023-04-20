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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Smart Mirror')
        self.setStyleSheet("background-color: {};".format(settings.mainwindowcolor))

        self.showhideThemesButton = QPushButton('Toggle Theme Selector', self)
        self.showhideThemesButton.setStyleSheet("font: 15pt Arial; color: white; background-color: black")
        self.showhideThemesButton.setGeometry(1300, 820, 225, 50)
        self.showhideThemesButton.clicked.connect(self.toggle_ThemeSelector)
        # makes a timer to update the theme colors for mainwindow and the theme selector push button
        self.updateMainWindowColorAndThemeButtonColortimer = QTimer(self) # makes a timer
        self.updateMainWindowColorAndThemeButtonColortimer.timeout.connect(self.updateMainWindowColorAndThemeButtonColor) #connects the timer to the updateMainWindowColorAndThemeButtonColor def (function)
        self.updateMainWindowColorAndThemeButtonColortimer.start(1000) # 1000ms = 1 second
        self.updateMainWindowColorAndThemeButtonColor() # runs updateMainWindowColorAndThemeButtonColor initially to get rid of delay at program start

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

        self.calendar_widget = CalendarWidget(self)
        self.calendar_widget.move(500,500)
        self.calendar_widget.setMinimumSize(500, 500)

    def toggle_ThemeSelector(self):
        if settings.themewindowswitcher == 1:
            self.theme_widget.hide()
            settings.themewindowswitcher = 0
        elif settings.themewindowswitcher == 0:
            self.theme_widget.show()
            settings.themewindowswitcher = 1

    def updateMainWindowColorAndThemeButtonColor(self):
        self.setStyleSheet("background-color: {};".format(settings.mainwindowcolor))
        self.showhideThemesButton.setStyleSheet("font: 15pt Arial;color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))

        

