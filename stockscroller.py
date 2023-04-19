from PyQt6.QtCore import QTimer, Qt, QPropertyAnimation, QRect
from stockwidget import StockWidget
from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

global offset 
offset = 0


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
            self.objs[i].move(offset, 0)
            print(rect)

            offset += (rect * 2 + 100)
            print(offset)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scrollStocks)
        self.timer.start(10000)
        self.scrollStocks()

    def scrollStocks(self):
        global xpos
        global offset
        self.anms = list()
        for i in range(len(self.objs)):
            rect = QRect(self.objs[i].pos(), self.objs[i].size())
            self.anms.append(QPropertyAnimation(self.objs[i], b'geometry'))
            self.anms[i].setDuration(10000)
            self.anms[i].setStartValue(rect)
            rect.moveLeft(2000)
            self.anms[i].setEndValue(rect)
            self.anms[i].start()
