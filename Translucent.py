
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

# http://stackoverflow.com/questions/1333610/displaying-translucent-irregular-shaped-windows-with-qt
# http://www.gnuton.org/blog/2011/01/transparent-qml-application/

class TranslucentView(QDeclarativeView):
    def __init__(self):
        QDeclarativeView.__init__(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.viewport().setAutoFillBackground(False)

    #def paintEvent(self, event):
    #    painter = QPainter(self)
    #    painter.setRenderHint(QPainter.Antialiasing)
    #    painter.setPen(Qt.NoPen)
    #    painter.setBrush(QColor(255, 0, 0, 127))
    #    painter.drawEllipse(0, 0, self.width(), self.height())

app = QApplication([])
view = TranslucentView()
view.setWindowTitle('Translucent QML Windows')
view.setSource(__file__.replace('.py', '.qml'))
view.show()
app.exec_()

