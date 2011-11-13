
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

import sys

app = QApplication(sys.argv)

class Provider(QObject):
    def __init__(self):
        QObject.__init__(self)

    @Slot(unicode, result='QVariant')
    def get_data(self, something):
        print 'get_data(', something, ') called'
        return [
                {'name': 'John', 'color': 'blue'},
                {'name': 'Bob', 'color': 'red'},
                {'name': something, 'color': 'green'}
        ]

provider = Provider()

view = QDeclarativeView()
view.rootContext().setContextProperty('provider', provider)
view.setSource(__file__.replace('.py', '.qml'))
view.show()

sys.exit(app.exec_())

