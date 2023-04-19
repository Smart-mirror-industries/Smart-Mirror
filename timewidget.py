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
       
        time_text = f"<span style='font-size: {settings.textsizenum}px'>{dateTime.toString('hh:mm')}</span>"
        date_text = f"<span style='font-size: {settings.textsizenum/2.25}px'>{dateTime.toString('MMMM d, yyyy')}</span>"
        text = f"<center>{time_text}<br>{date_text}</center>"

        self.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.setText(text)

        if settings.textsize == 'large':
            self.setFixedSize(225, 130)
        elif settings.textsize == 'medium':
            self.setFixedSize(150,100)
        elif settings.textsize == 'small':
            self.setFixedSize(100,50)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag_distance = event.pos() - self.drag_start_position
            self.move(self.x() + drag_distance.x(), self.y() + drag_distance.y())