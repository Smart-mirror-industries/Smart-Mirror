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
        self.label = QtWidgets.QLabel("It is {} and the current time is: {}".format(current_date, current_time))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet("QToolTip color: white;")

        # Create a layout for the widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


app = QtWidgets.QApplication(sys.argv)
current_time_and_date = CurrentTimeAndDate()
current_time_and_date.show()
sys.exit(app.exec())