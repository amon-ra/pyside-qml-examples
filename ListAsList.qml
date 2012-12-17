
import QtQuick 1.1

ListView {
    width: 500
    height: 500
    model: pylist
    delegate: Text {
        text: modelData.c
        MouseArea {
            anchors.fill: parent
            onClicked: mycontroller.pycallback(modelData.d)
        }
    }
}

