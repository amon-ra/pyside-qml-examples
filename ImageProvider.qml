
import Qt 4.7

Rectangle {
    width: 400
    height: 200
    color: '#ebbe47'

    Image {
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        // This uses the custom ImageProvider defined inside Python:
        source: 'image://python/ThisPartIsGivenAsIDToTheImageProvider'
    }

    Image {
        anchors.top: parent.top
        anchors.left: parent.left
        source: 'image://python/TheSecondImageIsTheSame'
        sourceSize { width: 10; height: 10 }
    }
}

