from PyQt6.QtCore import QTimer, Qt, QPropertyAnimation, QRect, QEventLoop
from stockwidget import StockWidget
from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
import time

global offset 
offset = 0
global recentUpdate


# class StockScroller(QOpenGLWidget)
class StockScroller(QGraphicsView):
    def __init__(self, parent):
        super(StockScroller, self).__init__(parent)

        # Initialize stock ticker classes
        tickers = []
        numtickers = input("# Of stocks you wish to track: ")

        for x in range(int(numtickers)):
            tickers.append(input("Input Ticker: "))

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.objs = list()
        for ticker in tickers:
            stock_widget = StockWidget(self, ticker)
            proxy_widget = QGraphicsProxyWidget()
            proxy_widget.setWidget(stock_widget)
            self.scene.addItem(proxy_widget)
            self.objs.append(stock_widget)

        for i in range(len(self.objs)):
            global offset
            rect = self.objs[i].fontMetrics().horizontalAdvance(self.objs[i].text())
            #self.objs[i].move(offset, 0)
            #print(rect)

            #offset += (rect * 2 + 100)
            offset+=rect
            print(offset)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateStocks)
        self.timer.start(10000)
        self.scrollStocks()
        self.updateStocks()
        

    def scrollStocks(self):
        global xpos
        global offset
        isOne = 0
        self.anms = list()
        for i in range(len(self.objs)):
            if i==1:
                isOne=1
            rect = QRect(self.objs[i].pos(), self.objs[i].size())
            self.anms.append(QPropertyAnimation(self.objs[i], b'geometry'))
            self.anms[i].setDuration(20000)
            self.anms[i].setStartValue(rect)
            rect.moveLeft(1920+offset)
            self.anms[i].setEndValue(rect)
            self.anms[i].setLoopCount(-1)
            #loop = QEventLoop()
            QTimer.singleShot(i*2000+1000*isOne, lambda i=i: self.anms[i].start())
            #QTimer.singleShot(200, loop.quit)
            #loop.exec()
    # Call resetPosition after animations have completed
        #self.timer.singleShot(20000, self.resetPosition)
    
    def updateStocks(self):
        for i in range(len(self.objs)):
            #if self.anms[i].currentTime()%20000>19900|self.anms[i].currentTime()%20000<100:
            #print(self.anms[i].currentValue().x())
            #if(self.anms[i].currentValue().x()==0):
            self.objs[i].updateStock()

        

if __name__ == '__main__':
    app = QApplication([])
    window = StockScroller()
    window.show()
    app.exec()