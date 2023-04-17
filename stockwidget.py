import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel
#import threading
#import time
#Assign Stocks of choice (Currently hardcoded)


#Print current ticker
#print('ticker: %s'%(ticker))

#global ticker
#ticker = 'IOVA'

#global xpos
#xpos = 0

global oldprice
oldprice = 0

# This class uses the label widget of PyQt6
class StockWidget(QLabel):

    def getticker(self):
        return self.ticker

    #def setticker(self,stock):
    #    print(stock)
    #    self.ticker = stock
    def setx(self,xpos):
    #   print(stock)
        self.xpos = xpos

    def getx(self):
    #   print(stock)
        return self.xpos
        
    def __init__(self, parent=None, ticker = 'IOVA'):
        super().__init__(parent)
        self.parent = parent
        self.ticker = ticker
        self.data = None
        self.data_formatted = {}
        self.oldtext = 'test'
        self.xpos = 0
        self.updateStock()

        #print(str(self.getticker() + "AAAAA: " + str(data_formatted[self.getticker() + '.currentPrice'].iloc[-1])))


        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white; background-color: rgba(255, 255, 255, 0)")

        # sets the size of the label so all the text can be seen
        self.setGeometry(0,0,1740,40) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignLeft) #if the MinSize is too big, the text position will not match the move command
        
        self.move(-500,0)           
    

    def updateStock(self):
        global oldprice
        yf_info = yf(self.getticker())     
        #Put data into dataframe
        data_formatted = pd.json_normalize(yf_info.financial_data)
        #self.oldtext = 
        self.setText(str(self.getticker() + ": " + str(data_formatted[self.getticker() + '.currentPrice'].iloc[-1]))) 
        self.update()
        #self.setIndent(self.getx())
        if data_formatted[self.getticker() + '.currentPrice'].iloc[-1]>oldprice:
            
            self.setStyleSheet("font: 25pt Arial; color: green; background-color: rgba(255, 255, 255, 0)")
        else:
            self.setStyleSheet("font: 25pt Arial; color: red; background-color: rgba(255, 255, 255, 0)")
        #print(oldprice)
        #print("OLDPRICE^")


        oldprice = data_formatted[self.getticker() + '.currentPrice'].iloc[-1]
    
