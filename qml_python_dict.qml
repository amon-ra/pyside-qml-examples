
import QtQuick 1.0

ListView {
    width: 400; height: 400

    model: provider.get_data('Click somewhere to load the model from Python')

    delegate: Text {
        text: modelData.name
        color: modelData.color
    }

    MouseArea {
        anchors.fill: parent
        onClicked: parent.model = provider.get_data(''+mouse.x+'/'+mouse.y)
    }
}

