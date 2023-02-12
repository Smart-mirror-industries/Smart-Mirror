
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QPalette
from timewidget import TimeWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Title
        self.setWindowTitle("Smart Mirror")

        # Set the background color of the window to white
        self.setStyleSheet("background-color: black;")
        

        # Create an instance of TimeWidget and set it as the central widget
        time_widget = TimeWidget()
        self.setCentralWidget(time_widget)