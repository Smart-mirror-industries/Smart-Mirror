import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt, QPropertyAnimation
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
            rect = self.objs[i].fontMetrics().horizontalAdvance(self.objs[i].text())
            #rect2 = self.objs[i].fontMetrics().horizontalAdvance(self.objs[i].text())
            #self.objs[i].move(200+200*i,0)
            self.objs[i].move(offset,0)
            print(rect)

            offset += (rect*2 + 100)#rect.width() + 50  # Add 10 pixels of padding between labels        
            print(offset)
        #offset = ogoffset
        self.timer = QTimer(self) # makes a timer
        
        self.timer.timeout.connect(self.scrollStocks) #connects the timer to the showTime def (function)
        self.timer.start(10000) # update every 8 ms = 120Hz
        self.scrollStocks() # runs showTime initially to get rid of delay at program start

    def printstuff(self):
        for i in range(len(self.objs)):
            print(self.objs[i].getx()) 
    def scrollStocks(self):
        global xpos
        global offset
        self.anms = list()
        for i in range(len(self.objs)):
            self.anms.append(QPropertyAnimation(self.objs[i], b'geometry'))
            self.anms[i].setDuration(5000)
            self.anms[i].setStartValue(self.objs[i].geometry().translated(0,0))
            self.anms[i].setEndValue(self.objs[i].geometry().translated(2000,0))
            self.anms[i].start()
            #If ticker is within boundary set new indent
            #if(xpos +self.objs[i].getx() <3000):
            #    self.objs[i].setIndent(xpos)   