# import pyqt6 stuff
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel


# import custom subclasses
from timewidget import TimeWidget
from MapWidget import MapWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Makes the main window and sets the background to black
        self.setWindowTitle('Smart Mirror')
        self.setStyleSheet("background-color: black;")

        time_widget = TimeWidget(self)
        time_widget.move(200, 200)

        map_widget = MapWidget(self)
        map_widget.setMinimumSize(300, 300)
        map_widget.move(800, 200)