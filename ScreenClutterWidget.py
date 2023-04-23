from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt6.QtCore import Qt, QTimer
import settings

class ScreenClutterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Create labels and checkboxes
        self.label1 = QLabel('Time Widget Visibility')
        self.checkbox1 = QCheckBox()
        self.label2 = QLabel('Weather Widget Visibility')
        self.checkbox2 = QCheckBox()
        self.label3 = QLabel('Map Widget Visibility')
        self.checkbox3 = QCheckBox()
        self.label4 = QLabel('Stock Widget Visibility')
        self.checkbox4 = QCheckBox()
        self.label5 = QLabel('Calender Widget Visibility')
        self.checkbox5 = QCheckBox()

        # Create layout for labels and checkboxes
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.checkbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.checkbox2)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.label3)
        hbox3.addWidget(self.checkbox3)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.label4)
        hbox4.addWidget(self.checkbox4)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.label5)
        hbox5.addWidget(self.checkbox5)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        # Set the font color of the text labels to match the theme
        self.label1.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label2.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label3.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label4.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label5.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.setStyleSheet("background-color: {};".format(settings.colorthemebackground))

        # Set the layout for the widget
        hbox1.setAlignment(Qt.AlignmentFlag.AlignRight)
        hbox2.setAlignment(Qt.AlignmentFlag.AlignRight)
        hbox3.setAlignment(Qt.AlignmentFlag.AlignRight)
        hbox4.setAlignment(Qt.AlignmentFlag.AlignRight)
        hbox5.setAlignment(Qt.AlignmentFlag.AlignRight)
        vbox.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setLayout(vbox)

        self.checkbox1.setCheckState(Qt.CheckState.Checked)
        self.checkbox2.setCheckState(Qt.CheckState.Checked)
        self.checkbox3.setCheckState(Qt.CheckState.Checked)
        self.checkbox4.setCheckState(Qt.CheckState.Checked)
        self.checkbox5.setCheckState(Qt.CheckState.Checked)

        # Connect checkbox signals to update global variables
        self.checkbox1.stateChanged.connect(lambda state, var=settings.timewidgetVisibility: setattr(settings, 'timewidgetVisibility', int(state == 2)))
        self.checkbox2.stateChanged.connect(lambda state, var=settings.timewidgetVisibility: setattr(settings, 'weatherwidgetVisibility', int(state == 2)))
        self.checkbox3.stateChanged.connect(lambda state, var=settings.timewidgetVisibility: setattr(settings, 'mapwidgetVisibility', int(state == 2)))
        self.checkbox4.stateChanged.connect(lambda state, var=settings.timewidgetVisibility: setattr(settings, 'stockwidgetVisibility', int(state == 2)))
        self.checkbox5.stateChanged.connect(lambda state, var=settings.timewidgetVisibility: setattr(settings, 'calenderwidgetVisibility', int(state == 2)))
        
        # makes a timer to update the theme every second
        self.timer = QTimer(self) # makes a timer
        self.timer.timeout.connect(self.screenclutterUpdateTheme) #connects the timer to the screenclutterUpdateTheme def (function)
        self.timer.start(1000) # 1000ms = 1 second
        self.screenclutterUpdateTheme() # runs screenclutterUpdateTheme initially to get rid of delay at program start

    def screenclutterUpdateTheme(self):
        self.label1.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label2.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label3.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label4.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))
        self.label5.setStyleSheet("color: {}; background-color: {};".format(settings.colorthemetext, settings.colorthemebackground))