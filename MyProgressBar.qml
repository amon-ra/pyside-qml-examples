
import Qt 4.7

Rectangle {
    id: progressBar
    color: "#aaa"
    height: 20

    property real progress: 0
    property int size: 0

    function formatProgress(size, progress) {
        return "" + parseInt(progress*size/1024) +
            " KiB ("+parseInt(progress*100.) + "%)";
    }


    Rectangle {
        color: progressBar.progress<1?"#ee8":"#8e8"
        clip: true

        anchors {
            top: parent.top
            bottom: parent.bottom
            left: parent.left
        }

        width: parent.width*progressBar.progress

        Text {
            anchors {
                fill: parent
                rightMargin: 5
            }
            color: "black"
            text: formatProgress(progressBar.size, progressBar.progress)
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignRight
        }
    }
}

