
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

import sys

app = QApplication(sys.argv)

class MyObject(QObject):
    def __init__(self):
        QObject.__init__(self)

a = MyObject()
b = MyObject()

pylist = [
    {'a': 1, 'b': 'Two', 'c': 3.3, 'd': a},
    {'a': 11, 'b': 'Two Two', 'c': 6.6, 'd': b},
]

class MyController(QObject):
    @Slot(QObject)
    def pycallback(self, o):
        print 'got:', o

mycontroller = MyController()

view = QDeclarativeView()
view.rootContext().setContextProperty('pylist', pylist)
view.rootContext().setContextProperty('mycontroller', mycontroller)
view.setSource(__file__.replace('.py', '.qml'))
view.show()

sys.exit(app.exec_())

