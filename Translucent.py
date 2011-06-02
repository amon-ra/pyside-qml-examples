
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

class TranslucentView(QDeclarativeView):
    def __init__(self):
        QDeclarativeView.__init__(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.viewport().setAutoFillBackground(False)

app = QApplication([])
view = TranslucentView()
view.setWindowTitle('Translucent QML Windows')
view.setSource(__file__.replace('.py', '.qml'))
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
view.showFullScreen()
app.exec_()

