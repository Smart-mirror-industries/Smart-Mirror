from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QDateTime, Qt, QTimer
from PyQt6.QtGui import QFont, QFontDatabase


class TimeWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a vertical layout
        layout = QVBoxLayout()
        
        #Change font size (Font selection does not affect displayed font)
        font = QFont("Serif", 50)
        font.Weight(1000) #Currently does not affect the Font weight
        #font.weight: 200
        
        # Create a label to display the current date and time
        self.label = QLabel()
        # self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setStyleSheet("QLabel { color : white; }")

        # Set the layout + font
        self.setLayout(layout)
        self.label.setFont(font)

        # Set the timer to update the label every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

        

    def update_time(self):
        # Get the current date and time
        datetime = QDateTime.currentDateTime()

        # Format the date and time as a string
        text = datetime.toString()

        # Update the label
        self.label.setText(text)
