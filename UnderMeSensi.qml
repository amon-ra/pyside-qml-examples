import Qt 4.7

Rectangle {
    width: 800
    height: 480

    Image {
        id: img
        source: "images/pysidelogo.png"
        fillMode: Image.PreserveAspectFit
        width: parent.width/2
        height: parent.height/2
        anchors.centerIn: parent
        transform: [
            Rotation {
                origin {
                    x: img.width/2
                    y: img.height/2
                }
                axis { x: 1; y: 0; z: 0 }
                angle: listener.tilt
            },
            Rotation {
                origin {
                    x: img.width/2
                    y: img.height/2
                }
                axis { x: 0; y: 0; z: 1 }
                angle: listener.rotation
            }
        ]
    }

    Text {
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        color: "#aaa"
        text: "To quit, press Ctrl+Backspace, then close"
    }
}

