import csv
from PyQt6.QtCore import QDateTime, QTimer, Qt
from PyQt6.QtGui import QPalette, QColor, QFont
from PyQt6.QtWidgets import QLabel, QTextEdit #qtextedit may be needed later

# This class uses the label widget of PyQt6
class reminderwidget(QLabel): #Thank you Jack for most of this templete.
    def __init__(self, parent=None):
        super().__init__(parent)

        # sets the font size, font, and color (** must be white to show on black mainwindow **)
        self.setStyleSheet("font: 12pt Arial; color: white")

        # sets the size of the label so all the text can be seen
        self.setMinimumSize(400, 200) # Slowly increase until all text is visible
        
        # aligns the text to be in the center of the label
        self.setAlignment(Qt.AlignmentFlag.AlignCenter) #if the MinSize is too big, the text position will not match the move command
                                                        #because it will be centering the text to the middle of the large label
        #everything above is fine to keep
        
        # makes a timer to update the time every second
        #self.timer = QTimer(self) # makes a timer
        #self.timer.timeout.connect(self.showReminders) #connects the timer to the showTime def (function)
        #self.timer.start(1000) # 1000ms = 1 second #Im keeping this for future use possibly
        self.showReminders() # display

    # function that "re-draws" the widget so it displays the time every new second
    def showReminders(self):
        #Currently you open up the txt file to edit it.  Not sure how that could work with the mirror
        with open('reminders.txt', 'r') as reminder_file: #Open the txt to read
            text = reminder_file.read()
        #I see now Ryan wanted a dynamic list you can expand and shrink and type things into
        self.setText(text)
    
        
