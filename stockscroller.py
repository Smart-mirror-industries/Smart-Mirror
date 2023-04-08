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
        self.timer.start(8) # update every 8 ms = 120Hz
        self.scrollStocks() # runs showTime initially to get rid of delay at program start
        
    def scrollStocks(self):
        global xpos
        global offset
        
        ogoffset = offset
        print(ogoffset)

        #if (xpos == 3000):
        #    xpos = 0
        #    for i in range(len(self.objs)):
        #        self.objs[i].updateStock()

        ended = 0
        for i in range(len(self.objs)):
            #If ticker is within boundary set new indent
            if(xpos +self.objs[i].getx() <3000):
                self.objs[i].setIndent(xpos)   
                #print(xpos)
            else: # If the Ticker has exceeded the boundary, move the ticker to be the next loopback 
                #if (ended == 0):
                self.objs[i].move(offset,0)
                offset = offset - (self.objs[i].fontMetrics().horizontalAdvance(self.objs[i].text())*2+100)
                ended= ended + 1
                print("Current offset: %d \t Current Ticker: %s", offset, self.objs[i].text())
                if(ended==(len(self.objs)-1)): # If the last ticker has exceeded boundary, reset xposition
                    xpos = 0
                    print(ended)
                #else:
                    
                    
            
        offset = ogoffset
        xpos +=5
        #self.timer.stop()