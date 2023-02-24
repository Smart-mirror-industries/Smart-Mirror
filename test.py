import json
import pandas as pd
from yahooquery import Ticker as yf
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel

yf_info = yf('MSFT')
olddata = yf_info.financial_data

#Put data into dataframe
data_formatted = pd.json_normalize(olddata)
while 1:
    print(data_formatted.columns.tolist())