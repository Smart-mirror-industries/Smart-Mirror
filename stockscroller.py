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
            self.objs[i].move(200+200*i,0)
        
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.scrollStocks) #connects the timer to the showTime def (function)
        self.timer.start(8) # update every 8 ms = 120Hz
        self.scrollStocks() # runs showTime initially to get rid of delay at program start
        
    def scrollStocks(self):
        global xpos
        objflag = 0

        if (xpos == 3000):
            xpos = 0
            for i in range(len(self.objs)):
                self.objs[i].updateStock()

        
        #print(oldtext)
        for i in range(len(self.objs)):
            self.objs[i].setIndent(xpos)
            if((self.objs[i].x()+xpos) > 2000):
                self.objs[i].move(xpos-200,0)
                if(i!=objflag):
                    self.objs[i].move(xpos+200,0)
                objflag = i
            

            
        
        xpos = xpos + 1
        #self.timer.stop()