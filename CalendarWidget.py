from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from Calendar import Ui_Form


class CalendarWidget(QWidget):

    
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent)
        
        # Create an instance of the Ui_Form class
        self.ui = Ui_Form()
        #self.setMinimumSize(250, 700)
        # Call the setupUi() method and pass the current instance of MyForm as an argument
        self.ui.setupUi(self)
        # Create a vertical layout and add the CalendarWidget to it
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui.calendarWidget)
        self.move(400,400)