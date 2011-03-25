
# Custom Image Provider for QML, written in PySide

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

class ImageProvider(QDeclarativeImageProvider):
    IMAGE_TYPE = QDeclarativeImageProvider.ImageType.Image

    def __init__(self):
        QDeclarativeImageProvider.__init__(self, ImageProvider.IMAGE_TYPE)

    def requestImage(self, id, size, requestedSize):
        print 'requestImage:', {
                'id': id,
                'size': size,
                'requestedSize': requestedSize
        }
        return QImage('images/pysidelogo.png')

app = QApplication([])
view = QDeclarativeView()

provider = ImageProvider()
view.engine().addImageProvider('python', provider)

view.setSource(__file__.replace('.py', '.qml'))

view.show()
app.exec_()

