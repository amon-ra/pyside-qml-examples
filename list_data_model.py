
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

#data wrapper
class Line(object):
    
    def __init__(self, title, text):
        self.title = title
        self.text = text

#list model for qml        
class TestLineModel(QAbstractListModel):
    TITLE_ROLE = Qt.UserRole + 1
    TEXT_ROLE = Qt.UserRole + 2

    def __init__(self, parent=None):
        super(TestLineModel, self).__init__(parent)
        self._data = []
        
        #register roles (names one can use from qml)
        keys = {}
        keys[TestLineModel.TITLE_ROLE] = 'title'
        keys[TestLineModel.TEXT_ROLE] = 'text'
        self.setRoleNames(keys)
        
    def rowCount(self, index):
        return len(self._data)
        
    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._data):
            return None
            
        line = self._data[index.row()]
        
        if role == TestLineModel.TITLE_ROLE:
            return line.title
        elif role == TestLineModel.TEXT_ROLE:
            return line.text
        else:
            return None
          
    @Slot()
    def add(self):
        count = len(self._data)        
        self.beginInsertRows(QModelIndex(), count, count) #notify view about upcoming change        
        self._data.append(Line('title # {0}'.format(count),'text #{0}'.format(count)))
        self.endInsertRows() #notify view that change happened
        
    @Slot()
    def remove(self):
        if len(self._data) > 0:
            position = len(self._data) -1
            self.beginRemoveRows(QModelIndex(), position, position) #notify view about upcoming change
            self._data.pop()
            self.endRemoveRows() #notify view that change happened


app = QApplication(sys.argv)
view = QDeclarativeView()
listModel = TestLineModel()

#add some data to the model
listModel.add()
listModel.add()
listModel.add()

#expose model to qml
context = view.rootContext()
context.setContextProperty('list', listModel)

view.setSource(__file__.replace('.py', '.qml'))
view.show()

sys.exit(app.exec_())
