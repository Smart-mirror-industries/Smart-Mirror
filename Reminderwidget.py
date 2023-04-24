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

        vbox1 = QVBoxLayout() #Holder for the text
        vbox2 = QVBoxLayout() #To stack both of these into each other?

        hbox1 = QHBoxLayout()#Holder for the buttons

        hbox1.addWidget(self.add_button)
        hbox1.addWidget(self.delete_button)

        vbox2.addLayout(hbox1)
        vbox2.addLayout(vbox1)

        

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

        
    def add_textbox(self):#this creates text boxes
        # Create a new QLineEdit widget
        textbox = QLineEdit()
        
        # Add the text box to the layout
        self.vbox1.addWidget(textbox)
        
    def delete_textbox(self): #removes the last created text box, if there's no boxes it crashes
        
        self.vbox1.takeAt(self.textbox_layout.count() - 1).widget().deleteLater()