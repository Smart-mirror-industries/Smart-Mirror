import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class mainUI(QWidget):
    def __init__(self):
        super().__init__()

        #Set Background
        self.setStyleSheet("background-color: black;") 

        #Set Fullscreen
        self.showFullScreen()
        
        #Toggle Visibility
        self.show()
        

app = QApplication(sys.argv)

window = mainUI()

app.exec()