import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

from stockwidget import StockWidget
from PyQt6.QtWidgets import QMainWindow, QWidget
#import threading
#import multiprocessing
global xpos
xpos = 0
global delay
delay = 0
global offset
offset = 0


class StockScroller(QWidget):
    def __init__(self,parent):
        super(StockScroller,self).__init__(parent)

        #Initialize stock ticker classes
        tickers = []
        numtickers = input("# Of stocks you wish to track: ")

        for x in range(int(numtickers)):
            tickers.append(input("Input Ticker: "))

        self.objs = list()
        for ticker in tickers:
            self.objs.append(StockWidget(self,ticker))
        for i in range(len(self.objs)):
            global offset
            rect = self.objs[i].fontMetrics().boundingRect(self.objs[i].text())
            #self.objs[i].move(200+200*i,0)
            self.objs[i].move(offset,0)
            print(rect)

            offset += rect.width() + 50  # Add 10 pixels of padding between labels        
            print(offset)
        
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.scrollStocks) #connects the timer to the showTime def (function)
        self.timer.start(8) # update every 8 ms = 120Hz
        self.scrollStocks() # runs showTime initially to get rid of delay at program start
        
    def scrollStocks(self):
        global xpos

        if (xpos == 3000):
            xpos = 0
            for i in range(len(self.objs)):
                self.objs[i].updateStock()

        for i in range(len(self.objs)):
            self.objs[i].setIndent(xpos)
        
        xpos = xpos + 1
        #self.timer.stop()