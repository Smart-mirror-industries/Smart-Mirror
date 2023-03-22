# import pyqt6 stuff
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel


# import custom subclasses
from timewidget import TimeWidget
from MapWidget import MapWidget
from stockscroller import StockScroller
from Weatherwidget import weatherwidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Makes the main window and sets the background to black
        self.setWindowTitle('Smart Mirror')
        self.setStyleSheet("background-color: black;")

        # Create the time widget and add it to the main window
        self.time_widget = TimeWidget(self)
        self.moveTimeWidget(0, 100) #moves the timewidget using the unique def below
        self.stock_scroller = StockScroller(self)
        self.stock_scroller.setMinimumSize(3000, 50)

        self.weather_widget = weatherwidget(self)
        self.moveWeatherWidget(75,200)

        
        self.stock_scroller.move(-200, 50)
        #self.stock_widget = StockWidget(self)
        #self.stock_widget2 = StockWidget(self)
        #self.stock_widget3 = StockWidget(self)
        #self.stock_widget.setticker('DIS')
        #self.stock_widget2.setticker('MSFT')
        #self.stock_widget3.setticker('ZIM')
        #self.moveStockWidget(0, 0)

        map_widget = MapWidget(self)
        map_widget.setMinimumSize(300, 300)
        map_widget.move(800, 200)
        
        #Create the x widget and add it to the main window
        


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


