
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

class Forwarder(QObject):
    def __init__(self):
        QObject.__init__(self)

    # This signal can be emitted from Python and connected to from QML
    doSomething = Signal()

app = QApplication(sys.argv)
view = QDeclarativeView()
forwarder = Forwarder()

context = view.rootContext()
context.setContextProperty('forwarder', forwarder)

view.setSource(__file__.replace('.py', '.qml'))
view.show()

def timer_on_timeout():
    print 'Doing something from Python...'
    # Emit the signal (will be received by QML)
    forwarder.doSomething.emit()

timer = QTimer()
timer.timeout.connect(timer_on_timeout)
timer.start(1000)

sys.exit(app.exec_())

