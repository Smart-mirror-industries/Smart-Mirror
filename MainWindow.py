# import pyqt6 stuff
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


# import custom subclasses
from timewidget import TimeWidget
from MapWidget import MapWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Makes the main window and sets the background to black
        self.setWindowTitle('Smart Mirror')
        self.setStyleSheet("background-color: black;")

        #set up grid widget layout
        layout = QGridLayout()

        #add widgets to grid
        layout.addWidget(TimeWidget(self), 0,0)
        layout.addWidget(MapWidget(), 2,1)

        #set the layout up to succesfully show
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        


