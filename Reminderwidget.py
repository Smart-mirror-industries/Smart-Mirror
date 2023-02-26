import csv
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QLabel, QTextEdit

# This class uses the label widget of PyQt6
class reminderwidget(QLabel): #Thank you Jack for most of this templete.
    def __init__(self, parent=None):
        super().__init__(parent)

        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 25pt Arial; color: white")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(400, 200) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) #if the MinSize is too big, the text position will not match the move command
                                                        #because it will be centering the text to the middle of the large label
        #everything above is fine to keep ngl

        # makes a timer to update the time every second
       # self.timer = QTimer(self) # makes a timer
        #self.timer.timeout.connect(self.showReminders) #connects the timer to the showTime def (function)
        #self.timer.start(1000) # 1000ms = 1 second
        self.showReminders() # display

    # function that "re-draws" the widget so it displays the time every new second
    def showReminders(self):
        with open('reminders.txt', 'r') as reminder_file:
            text = reminder_file.read()

        #text = ("This is a simple remidner:\n to take ur pills \n Wash the car") #Just a test
        
        self.setText(text)
    
        
