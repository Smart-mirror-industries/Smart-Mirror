#code from https://zetcode.com/pyqt/qwebengineview/

from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView



class MapWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):

        #set up widget layout
        vbox = QVBoxLayout(self)

        #call webEngineView, loadPage function
        self.webEngineView = QWebEngineView()
        self.loadPage()

        #add webEngineView to Layout
        vbox.addWidget(self.webEngineView)
        
        #set size and show
        self.setLayout(vbox)
        #self.setGeometry(300, 300, 350, 250)
        self.show()

    def loadPage(self):



        with open('maps.html', 'r', encoding='utf-8') as f: #this will call the maps API. DO NOT UNCOMMENT WHEN TESTING OTHER COMPONENETS
        #with open('test.html', 'r') as f: #placeholder code

            #read html file and load the page
            html = f.read()
            self.webEngineView.setHtml(html)