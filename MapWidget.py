#code from https://zetcode.com/pyqt/qwebengineview/

import os
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class MapWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):

        #set up widget layout
        vbox = QVBoxLayout(self)

        #call webEngineView, loadPage functions
        self.view = QWebEngineView()

        self.loadPage()

        #add webEngineView to Layout
        vbox.addWidget(self.view)
        
        #set size and show
        #self.setLayout(vbox)
        #self.setGeometry(300, 300, 350, 250)
        self.show()
        self.setMouseTracking(True)

    def onFeaturePermissionRequested(self, securityOrigin, feature):
        print("Location Requested")
        self.sender().setFeaturePermission(securityOrigin, QWebEnginePage.Feature.Geolocation, QWebEnginePage.PermissionPolicy.PermissionGrantedByUser)   

    def loadPage(self):
        with open('index.html', 'r', encoding='utf-8') as f: #this will call the maps API. DO NOT UNCOMMENT WHEN TESTING OTHER COMPONENETS
        #with open('test.html', 'r') as f: #placeholder code
            #read html file and load the page
            html = f.read()
            #self.view.setHtml(html, QUrl.fromLocalFile(full_path))
            self.view.setHtml(html, QUrl('https://maps.googleapis.com/maps/api/js?key=AIzaSyAUjbVnsLJroyFt1uKZbuoCY1UhNLSpyf4'))
            self.view.page().featurePermissionRequested.connect(self.onFeaturePermissionRequested)


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            drag_distance = event.pos() - self.drag_start_position
            self.move(self.x() + drag_distance.x(), self.y() + drag_distance.y())