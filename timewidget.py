from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
import sys
from datetime import datetime


class CurrentTimeAndDate(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the current date and time
        current_date = datetime.now().strftime("%B %d, %Y")
        current_time = datetime.now().strftime("%I:%M%p").lower()
        self.time = QtWidgets.QLabel("It is {} and the current time is: {}".format(current_date, current_time))
        self.time.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        font = self.time.font()
        font.setPointSize(30)
        self.time.setFont(font)
        self.time.show()
        #self.setStyleSheet("QToolTip color: white;")