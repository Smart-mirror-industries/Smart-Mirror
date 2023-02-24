#Import yahooquery (Yahoo Finance API is currently nonfunctional) 
import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

#Assign Stocks of choice (Currently hardcoded)


#Print current ticker
#print('ticker: %s'%(ticker))

#global ticker
#ticker = 'IOVA'

global olddata

global xpos
xpos = 0

# This class uses the label widget of PyQt6
class StockWidget(QLabel):

    def getticker(self):
        return self._ticker

    def setticker(self,stock):
        self._ticker = stock

    def __init__(self, parent=None, ticker = 'IOVA'):
        super().__init__(parent)
        self._ticker = ticker

        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white; background-color: rgba(255, 255, 255, 0)")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(1920, 100) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignLeft) #if the MinSize is too big, the text position will not match the move command
        
        self.move(-500,0)           

#Select desired data column and print
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.updateStock) #connects the timer to the showTime def (function)
        self.timer.start(8) # update every 8 ms = 120Hz
        self.updateStock() # runs showTime initially to get rid of delay at program start

    def updateStock(self):
        
        print(self.getticker())
        global xpos
        global olddata
        if (xpos == 1800):
            xpos = 0
        
        print(self.getticker()+'--------------------------------------------')
        if((xpos <= 5 )& (self.getticker()!='IOVA')):
            yf_info = yf(self.getticker())  
            data = yf_info.financial_data
            olddata = data
        print(olddata)
        #Put data into dataframe
        data_formatted = pd.json_normalize(olddata)
        text = str(self.getticker() + ": " + str(data_formatted[self.getticker() + '.currentPrice'].iloc[-1]))
        self.setText(text) 
        self.setIndent(xpos)
        xpos = xpos + 1