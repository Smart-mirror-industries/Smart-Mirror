from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit
import settings

class reminderwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):

        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete")#Establish buttons

        self.add_button.clicked.connect(self.add_textbox)
        self.delete_button.clicked.connect(self.delete_textbox)

        self.delete_button.setStyleSheet("background-color: white;")
        self.add_button.setStyleSheet("background-color: white;")

        self.vbox1 = QVBoxLayout() #Holder for the text
        vbox2 = QVBoxLayout() #To stack both of these into each other?

        hbox1 = QHBoxLayout()#Holder for the buttons

        hbox1.addWidget(self.add_button)
        hbox1.addWidget(self.delete_button)

        vbox2.addLayout(hbox1)#holds the buttons
        vbox2.addLayout(self.vbox1)#holds the text

       
        

        self.setLayout(vbox2)
        


        # set a layout for the boxes
        #self.textbox_layout = QVBoxLayout()
        
        #Set a layout for the buttons
        #self.button_layout = QHBoxLayout()
        
        # Create the "add" button
        #self.add_button = QPushButton("Add")
        #self.add_button.clicked.connect(self.add_textbox)
        
        # Create the "delete" button
        #self.delete_button = QPushButton("Delete")
        #self.delete_button.clicked.connect(self.delete_textbox)
        
        # Add the buttons to the button layout
        #self.button_layout.addWidget(self.add_button)
        #self.button_layout.addWidget(self.delete_button)
        
        # Add the layouts to the main window
        #self.setLayout(self.textbox_layout)
        #self.layout().addLayout(self.button_layout)

        self.setMouseTracking(True)

        
    def add_textbox(self):#this creates text boxes
        # Create a new QLineEdit widget
        textbox = QLineEdit()
        textbox.setStyleSheet("background-color: white;")
        # Add the text box to the layout
        self.vbox1.addWidget(textbox)
        
    def delete_textbox(self):
        if self.vbox1.count() > 0:
            self.vbox1.takeAt(self.vbox1.count() - 1).widget().deleteLater()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag_distance = event.pos() - self.drag_start_position
            self.move(self.x() + drag_distance.x(), self.y() + drag_distance.y())