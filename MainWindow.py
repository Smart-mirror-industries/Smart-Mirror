import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #title
        self.setWindowTitle("Smart Mirror")

        #style sheet
        self.setStyleSheet("background-color: black;")


        #set window size
        self.showMaximized()