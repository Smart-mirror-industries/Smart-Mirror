#Import yahooquery (Yahoo Finance API is currently nonfunctional) 
import json
import pandas as pd
from yahooquery import Ticker as yf

#Assign Stocks of choice (Currently hardcoded)
ticker = 'MSFT'

#Print current ticker
print('ticker: %s'%(ticker))
yf_info = yf(ticker)

#Grab Ticker Data
data = yf_info.financial_data

#Put data into dataframe
data_formatted = pd.json_normalize(data)

#Select desired data column and print
print("Price: ",data_formatted[ticker + '.currentPrice'].iloc[-1])