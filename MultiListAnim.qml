
import Qt 4.7
import "colibri"

Rectangle {
    width: 300
    height: 500
    CLSlider {
        id: slider
        width: parent.width
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        z: 2
    }
    ListView {
        z: 1
        anchors.top: slider.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        id: pythonList
        model: pythonListModel

        delegate: Component {
            Rectangle {
                width: pythonList.width
                height: 20 + slider.value
                gradient: Gradient {
                    GradientStop { position: 0; color: model.zenItem.checked?"#00B8F5":(index%2?"#eee":"#ddd") }
                    GradientStop { position: .93; color: model.zenItem.checked?"#0080A0":"#eee" }
                    GradientStop { position: 1; color: "#666" }
                }
                Text {
                    elide: Text.ElideRight
                    text: model.zenItem.name
                    color: (model.zenItem.checked?"white":"black")
                    anchors {
                        verticalCenter: parent.verticalCenter
                        left: parent.left
                        right: (model.zenItem.checked?checkbox.left:parent.right)
                        leftMargin: 5
                    }
                }
                Text {
                    id: checkbox
                    z: 5
                    text: "✔"
                    font.pixelSize: parent.height
                    font.bold: true
                    visible: model.zenItem.checked
                    transformOrigin: Item.Right
                    color: "white"
                    anchors {
                        verticalCenter: parent.verticalCenter
                        right: parent.right
                        rightMargin: 5
                    }
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: { controller.toggled(pythonListModel, model.zenItem, checkbox, parent) }
                }
            }
        }
    }
}

