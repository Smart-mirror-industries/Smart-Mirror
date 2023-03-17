import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
from time import sleep

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowmain = MainWindow()
    windowmain.showFullScreen()
    sys.exit(app.exec())

