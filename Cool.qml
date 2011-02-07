
import Qt 4.7

Rectangle {
    property string text: "..."
    color: "blue"
    height: 40

    Text {
        text: parent.text
        anchors.fill: parent
        color: "red"
    }
}
