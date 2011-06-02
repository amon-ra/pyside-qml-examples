#!/usr/bin/python

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

import StringIO
import sys

class Python(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.locals = {}
        self.globals = {}
        self._stdout = StringIO.StringIO()
        sys.stdout.close()
        sys.stdout = self._stdout
        sys.stderr.close()
        sys.stderr = self._stdout

    changed = Signal()

    def _get_output(self):
        return self._stdout.getvalue()

    output = Property(str, fget=_get_output, notify=changed)

    @Slot(str)
    def evaluate(self, value):
        print '>>>', value
        eval(compile(value, '<input>', 'single'), self.locals, \
                self.globals)

app = QApplication(sys.argv)

python = Python()

view = QDeclarativeView()
view.rootContext().setContextProperty('python', python)
view.setSource(__file__.replace('.py', '.qml'))
view.showFullScreen()

app.exec_()

