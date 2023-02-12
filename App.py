# https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
from PyQt6.QtWidgets import QApplication

import MainWindow

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow.MainWindow()
window.showFullScreen()

# Start the event loop.
app.exec()