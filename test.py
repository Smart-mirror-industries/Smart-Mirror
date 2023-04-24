from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from CalendarWidget import CalendarWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar Widget')
        
        # Create an instance of the CalendarWidget class
        self.calendar_widget = CalendarWidget()
        
        # Set the central widget of the main window to the CalendarWidget
        self.setCentralWidget(self.calendar_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())