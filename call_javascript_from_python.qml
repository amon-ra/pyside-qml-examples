
import QtQuick 1.0

Rectangle {
    width: 200
    height: 200

    Connections {
        target: forwarder
        onDoSomething: {
            // This is called whenever the "forwarder" in Python
            // emits the "doSomething" signal -> do something here
            console.log('...and do something else in QML.')
            text.rotation += 45
        }
    }

    Text {
        id: text
        anchors.centerIn: parent
        text: 'Call Javascript\nFrom Python'
        Behavior on rotation { RotationAnimation { } }
    }
}

