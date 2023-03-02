import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

from stockwidget import StockWidget
from PyQt6.QtWidgets import QMainWindow, QWidget
import threading
global xpos
xpos = 0

class StockScroller(QWidget):
    def __init__(self,parent):
        super(StockScroller,self).__init__(parent)

        #Initialize stock ticker classes
        self.stock_widget = StockWidget(self,'MSFT')
        self.stock_widget2 = StockWidget(self,'DIS')
        self.stock_widget3 = StockWidget(self,'HOOD')
        #self.stock_widget4 = StockWidget(self,'AMD')
        
        #Set stock tickers
        #self.stock_widget.setticker('DIS')
        #self.stock_widget2.setticker('MSFT')
        #self.stock_widget3.setticker('ZIM')

        #Assign stock positions (Will dynamically assign positions later)
        self.stock_widget2.move(-200,0)
        self.stock_widget3.move(100,0)
        #self.moveStockWidget(0, 0)
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.scrollStocks) #connects the timer to the showTime def (function)
        self.timer.start(8) # update every 8 ms = 120Hz
        self.scrollStocks() # runs showTime initially to get rid of delay at program start
        background_thread = threading.Thread(target=self.stock_widget.background_task)
        background_thread.daemon = True
        background_thread.start()
        background_thread2 = threading.Thread(target=self.stock_widget2.background_task)
        background_thread2.daemon = True
        background_thread2.start()
        background_thread3 = threading.Thread(target=self.stock_widget3.background_task)
        background_thread3.daemon = True
        background_thread3.start()
        
    def scrollStocks(self):
        global xpos
        if (xpos == 3000):
            xpos = 0
        
        #print(oldtext)
        self.stock_widget.setIndent(xpos)
        self.stock_widget2.setIndent(xpos)
        self.stock_widget3.setIndent(xpos)
        
        xpos = xpos + 2