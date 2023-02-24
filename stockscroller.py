import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

from stockwidget import StockWidget
from PyQt6.QtWidgets import QMainWindow, QWidget


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