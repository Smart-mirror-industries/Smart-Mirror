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

global xpos
xpos = 0

#global oldtext
#oldtext = 'test'

# This class uses the label widget of PyQt6
class StockWidget(QLabel):

    def getticker(self):
        return self.ticker

    #def setticker(self,stock):
    #    print(stock)
    #    self.ticker = stock

    def __init__(self, parent=None, ticker = 'IOVA'):
        super().__init__(parent)
        self.parent = parent
        self.ticker = ticker
        self.data = None
        self.data_formatted = {}
        self.oldtext = 'test'
        self.updateStock()

        #print(str(self.getticker() + "AAAAA: " + str(data_formatted[self.getticker() + '.currentPrice'].iloc[-1])))


        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white; background-color: rgba(255, 255, 255, 0)")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(3000, 100) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignLeft) #if the MinSize is too big, the text position will not match the move command
        
        self.move(-500,0)           

#Select desired data column and print
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.updateStock) #connects the timer to the showTime def (function)
        self.timer.start(8) # update every 8 ms = 120Hz
        self.updateStock() # runs showTime initially to get rid of delay at program start

    def updateStock(self):
        
        global xpos
        global oldtext

        if (xpos == 3000):
            xpos = 0
        #print(oldtext)
        
        if(xpos == 0): 
            yf_info = yf(self.getticker())     
            #Put data into dataframe
            data_formatted = pd.json_normalize(yf_info.financial_data)
            self.oldtext = str(self.getticker() + ": " + str(data_formatted[self.getticker() + '.currentPrice'].iloc[-1]))
        self.setText(self.oldtext) 
        self.setIndent(xpos)
        xpos = xpos + 1
