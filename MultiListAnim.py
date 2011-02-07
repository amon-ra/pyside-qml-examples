# -*- coding: utf-8 -*-

"""Animate your code of PySide"""

import sys

from PySide import QtCore
from PySide import QtGui
from PySide import QtDeclarative
from PySide import QtOpenGL

class ZenWrapper(QtCore.QObject):
    def __init__(self, zenItem):
        QtCore.QObject.__init__(self)
        self._zenItem = zenItem
        self._checked = False

    def _name(self):
        return self._zenItem

    def is_checked(self):
        return self._checked

    def toggle_checked(self):
        self._checked = not self._checked
        self.changed.emit()
        return self._checked

    changed = QtCore.Signal()

    name = QtCore.Property(unicode, _name, notify=changed)
    checked = QtCore.Property(bool, is_checked, notify=changed)

class ZenListModel(QtCore.QAbstractListModel):
    def __init__(self, zenItems):
        QtCore.QAbstractListModel.__init__(self)
        self._zenItems = zenItems
        self.setRoleNames({0: 'zenItem'})

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._zenItems)

    def checked(self):
        return [x for x in self._zenItems if x.checked]

    def data(self, index, role):
        if index.isValid() and role == 0:
            return self._zenItems[index.row()]

class Controller(QtCore.QObject):
    @QtCore.Slot(QtCore.QObject, QtCore.QObject, QtCore.QObject, QtCore.QObject)
    def toggled(self, model, wrapper, checkbox, parent):
        global view, __doc__
        new_value = wrapper.toggle_checked()
        new_list = model.checked()
        print '='*20, 'New List', '='*20
        print '\n'.join(x.name for x in new_list)
        view.setWindowTitle('%s (%d)' % (__doc__, len(new_list)))

        if new_value:
            pa = QtCore.QSequentialAnimationGroup(parent)
            anim = QtCore.QPropertyAnimation(checkbox, 'scale')
            anim.setDuration(700)
            anim.setStartValue(10)
            anim.setEndValue(1)
            anim.setEasingCurve(QtCore.QEasingCurve.OutSine)
            pa.addAnimation(anim)
            anim = QtCore.QPropertyAnimation(parent, 'rotation', parent)
            anim.setDuration(100)
            anim.setStartValue(-180)
            anim.setEndValue(0)
            pa.addAnimation(anim)
            pa.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

zenItems = [ZenWrapper(zenItem.rstrip()) for zenItem in open(__file__) if zenItem.strip() and not zenItem.startswith(' ')]

controller = Controller()
zenItemList = ZenListModel(zenItems)

app = QtGui.QApplication(sys.argv)

view = QtDeclarative.QDeclarativeView()
glw = QtOpenGL.QGLWidget()
view.setViewport(glw)
view.setWindowTitle(__doc__)
view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

rc = view.rootContext()

rc.setContextProperty('controller', controller)
rc.setContextProperty('pythonListModel', zenItemList)
view.setSource(__file__.replace('.py', '.qml'))

view.show()
app.exec_()

