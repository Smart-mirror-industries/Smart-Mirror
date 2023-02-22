#Import yahooquery (Yahoo Finance API is currently nonfunctional) 
import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

#Assign Stocks of choice (Currently hardcoded)
ticker = 'MSFT'

#Print current ticker
print('ticker: %s'%(ticker))

global olddata
global xpos
xpos = 0

# This class uses the label widget of PyQt6
class StockWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(250, 100) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) #if the MinSize is too big, the text position will not match the move command
                                                        #because it will be centering the text to the middle of the large label
        
        self.move(0,0)

#Select desired data column and print
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.updateStock) #connects the timer to the showTime def (function)
        self.timer.start(17) # 1000ms = 1 second
        self.updateStock() # runs showTime initially to get rid of delay at program start

    # function that "re-draws" the widget so it displays the time every new second
    def updateStock(self):
        global xpos
        xpos = xpos + 1
        
        
        yf_info = yf(ticker)
        print(xpos)
        
        data = yf_info.financial_data
        if xpos<=5:
        #Grab Ticker Data
            global olddata
            olddata = data

        #Put data into dataframe
        data_formatted = pd.json_normalize(olddata)
        text = str("MSFT: " + str(data_formatted[ticker + '.currentPrice'].iloc[-1]))
        self.setText(text) 
        self.move(xpos,0)
        self.update()
