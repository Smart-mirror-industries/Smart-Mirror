from PyQt6.QtCore import QDateTime, QTimer, Qt, QPoint
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel
import settings

class TimeWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) #if the MinSize is too big, the text position will not match the move command
                                                        #because it will be centering the text to the middle of the large label

        # makes a timer to update the time every second
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.showTime) #connects the timer to the showTime def (function)
        self.timer.start(1000) # 1000ms = 1 second
        self.showTime() # runs showTime initially to get rid of delay at program start

        
        self.setMouseTracking(True)

    # function that "re-draws" the widget so it displays the time every new second
    def showTime(self):
        dateTime = QDateTime.currentDateTime()
        # text = dateTime.toString('MMMM d, yyyy - hh:mm:ss') # time widget with seconds
        text = dateTime.toString('MMMM d, yyyy - hh:mm') # time widget without seconds
        self.setText(text)

        # checks the colortheme and the textsize and selects the matching Style Sheet
        # also sets the size of the widget based on the texstize
        if settings.colortheme == 'dark':
            if settings.textsize == 'large':
                self.setStyleSheet("font: 45pt Arial; color: white; background-color: black")
                self.setFixedSize(750, 45)
            elif settings.textsize == 'medium':
                self.setStyleSheet("font: 25pt Arial; color: white; background-color: black")
                self.setFixedSize(450, 30)
            elif settings.textsize == 'small':
                self.setStyleSheet("font: 10pt Arial; color: white; background-color: black")
                self.setFixedSize(200, 10) 
        elif settings.colortheme == 'light':
            if settings.textsize == 'large':
                self.setStyleSheet("font: 45pt Arial; color: black; background-color: white")
                self.setFixedSize(750, 45)
            elif settings.textsize == 'medium':
                self.setStyleSheet("font: 25pt Arial; color: black; background-color: white")
                self.setFixedSize(450, 30)
            elif settings.textsize == 'small':
                self.setStyleSheet("font: 10pt Arial; color: black; background-color: white")
                self.setFixedSize(200, 10) 
        elif settings.colortheme == 'gray':
            if settings.textsize == 'large':
                self.setStyleSheet("font: 45pt Arial; color: black; background-color: gray")
                self.setFixedSize(750, 45)
            elif settings.textsize == 'medium':
                self.setStyleSheet("font: 25pt Arial; color: black; background-color: gray")
                self.setFixedSize(450, 30)
            elif settings.textsize == 'small':
                self.setStyleSheet("font: 10pt Arial; color: black; background-color: gray")
                self.setFixedSize(200, 10) 
        else: print("Error with timewidget stylesheet - check the global variables in settings.py")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag_distance = event.pos() - self.drag_start_position
            self.move(self.x() + drag_distance.x(), self.y() + drag_distance.y())