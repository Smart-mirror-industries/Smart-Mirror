import sys
import timewidget

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #title
        self.setWindowTitle("Smart Mirror")

        #style sheet
        self.setStyleSheet("background-color: white;")

        #initialize time widget
        timeWidget = timewidget.CurrentTimeAndDate()

        # Create a layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(timeWidget)
        self.setLayout(layout)

        self.setCentralWidget(timeWidget)