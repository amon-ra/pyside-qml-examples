
import Qt 4.7


Item {
    width: 400
    height: 400
    Rectangle {
        color: 'black'
        anchors.fill: parent
        gradient: Gradient {
            GradientStop { position: 0; color: 'transparent' }
            GradientStop { position: 1; color: 'black' }
        }
        //opacity: .4
    }

    Image {
        id: rect
        //width: 200
        //height: 200
        anchors.centerIn: parent
        //opacity: .5
        source: 'images/pyside-rounded-corners.png'
        //color: 'red'

        RotationAnimation {
            target: rect
            property: 'rotation'
            from: 0
            to: 360
            loops: Animation.Infinite
            running: true
            duration: 2500
        }

        SequentialAnimation {
            running: true
            loops: Animation.Infinite
            PropertyAnimation {
                target: rect
                property: 'scale'
                from: 1
                to: 2
                duration: 1000
                easing.type: Easing.OutBounce
            }
            PropertyAnimation {
                target: rect
                property: 'scale'
                from: 2
                to: 1
                duration: 2500
                easing.type: Easing.OutExpo
            }
        }
    }
}

