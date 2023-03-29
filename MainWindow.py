# import pyqt6 stuff
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton


# import custom subclasses
from timewidget import TimeWidget
from stockscroller import StockScroller
from Weatherwidget import weatherwidget
from MapWidget import MapWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Smart Mirror')
        self.setStyleSheet("background-color: black;")

        # Set up the start button
        self.startbutton = QPushButton('Show Widgets', self)
        self.startbutton.setStyleSheet("font: 20pt Arial; color: white; background-color: black")
        self.startbutton.setGeometry(50, 50, 300, 50)
        self.startbutton.clicked.connect(self.show_widgets)

        # Create the time widget and add it to the main window
        self.time_widget = TimeWidget(self)
        self.moveTimeWidget(0, 100) #moves the timewidget using the unique def below
        self.time_widget.hide()

        self.stock_scroller = StockScroller(self)
        self.stock_scroller.setMinimumSize(3000, 50)

        self.weather_widget = weatherwidget(self)
        self.moveWeatherWidget(75,200)
        self.weather_widget.hide()
        
        self.stock_scroller.move(-200, 50)
        self.stock_scroller.hide()

        self.map_widget = MapWidget(self)
        self.moveMapWidget(300,200)
        self.map_widget.setMinimumSize(500, 500)
        self.map_widget.hide()

    def show_widgets(self):
        # Hide the button and show the labels
        self.startbutton.hide()
        self.time_widget.show()
        self.stock_scroller.show()
        self.weather_widget.show()
        self.map_widget.show()

    # use this def to add any widget to the mainwindow
    # do "self.widgetname = classname(self)" in the mainwindow constructor above
    def addWidget(self, widget):
        self.central_widget.layout().addWidget(widget) #adds the inputted widget to mainwindow (self)

    # To move specific widgets, create a def per widget using moveTimeWidget as a template:

    # moveTimeWidget is specifically for timewidget, each widget needs its own move def
    def moveTimeWidget(self, x, y):
        self.time_widget.move(x, y) # Moves the time widget to the specified position
    # moveTimeWidget is specifically for timewidget, each widget needs its own move def
    def moveStockWidget(self, x, y):
        self.stock_widget.move(x, y) # Moves the time widget to the specified position
    def moveWeatherWidget(self, x, y):
        self.weather_widget.move(x, y) # Moves the time widget to the specified position
    def moveMapWidget(self, x, y):
        self.map_widget.move(x,y)


