from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit
from PyQt6.QtGui import QPalette, QColor
import settings

class ThemeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
        # create a vertical layout to hold the widgets
        layout = QVBoxLayout(self)
        
        # create a label widget
        self.label = QLabel(self)
        layout.addWidget(self.label)
        
        # create three dropdown boxes
        self.colordropdown = QComboBox(self)
        self.textsizedropdown = QComboBox(self)
        # self.mainwindowcolordropdown = QComboBox(self)
        
        # add some options to the dropdown boxes
        self.colordropdown.addItems(["dark", "gray", "light"])
        self.textsizedropdown.addItems(["medium", "small", "large"])
        # self.mainwindowcolordropdown.addItems(["black", "gray", "white"])
        
        # add the dropdown boxes to the layout
        layout.addWidget(self.colordropdown)
        layout.addWidget(self.textsizedropdown)
        # layout.addWidget(self.mainwindowcolordropdown)

        self.colordropdown.setStyleSheet("font: 25pt Arial; color: white; background-color: black")
        self.textsizedropdown.setStyleSheet("font: 25pt Arial; color: white; background-color: black")
        # self.mainwindowcolordropdown.setStyleSheet("font: 25pt Arial; color: white; background-color: black")
        
        # connect the currentTextChanged signal of each dropdown box to a slot method
        self.colordropdown.currentTextChanged.connect(self.update_colortheme)
        self.textsizedropdown.currentTextChanged.connect(self.update_textsize)
        # self.mainwindowcolordropdown.currentTextChanged.connect(self.update_mainwindowbackground)

        self.stocks = QLineEdit(self)
        self.calendar = QLineEdit(self)
        layout.addWidget(self.stocks)
        layout.addWidget(self.calendar)
        self.stocks.setText("Comma Spearated Stocks:")
        self.calendar.setText("Enter Calendar Link:")
        self.stocks.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.calendar.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))

        self.update_colortheme(settings.colortheme)
        
    def update_colortheme(self, text):
        settings.colortheme = text
        #changing the color theme of themewidget:
        if text == 'dark':
            self.colordropdown.setStyleSheet("color: white; background-color: black")
            self.textsizedropdown.setStyleSheet("color: white; background-color: black")
            # self.mainwindowcolordropdown.setStyleSheet("color: white; background-color: black")
            self.stocks.setStyleSheet("color: white; background-color: black")
            self.calendar.setStyleSheet("color: white; background-color: black")
        elif text == 'gray':
            self.colordropdown.setStyleSheet("color: black; background-color: gray")
            self.textsizedropdown.setStyleSheet("color: black; background-color: gray")
            # self.mainwindowcolordropdown.setStyleSheet("color: black; background-color: gray")
            self.stocks.setStyleSheet("color: black; background-color: gray")
            self.calendar.setStyleSheet("color: black; background-color: gray")
        elif text == 'light':
            self.colordropdown.setStyleSheet("color: black; background-color: white")
            self.textsizedropdown.setStyleSheet("color: black; background-color: white")
            # self.mainwindowcolordropdown.setStyleSheet("color: black; background-color: white")
            self.stocks.setStyleSheet("color: black; background-color: white")
            self.calendar.setStyleSheet("color: black; background-color: white")
        
            

        if text == 'dark':
            settings.colorthemetext = 'white'
            settings.colorthemebackground = 'black'
            settings.mainwindowcolor = 'black'
        if text == 'gray':
            settings.colorthemetext = 'white'
            settings.colorthemebackground = 'gray'
            settings.mainwindowcolor = 'gray'
        if text == 'light':
            settings.colorthemetext = 'black'
            settings.colorthemebackground = 'white'
            settings.mainwindowcolor = 'white'
            

        

    def update_textsize(self, text):
        settings.textsize = text
        if text == 'medium':
            settings.textsizenum = 55
        if text == 'small':
            settings.textsizenum = 15
        if text == 'large':
            settings.textsizenum = 75

    # def update_mainwindowbackground(self, text):
    #     settings.mainwindowcolor = text