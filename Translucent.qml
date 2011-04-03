
import Qt 4.7


Item {
    width: 400
    height: 400
    Rectangle {
        id: rect
        width: 200
        height: 200
        anchors.centerIn: parent
        opacity: .5
        color: 'red'

        RotationAnimation {
            target: rect
            property: 'rotation'
            from: 0
            to: 360
            loops: Animation.Infinite
            running: true
            duration: 2500
        }
    }
}

