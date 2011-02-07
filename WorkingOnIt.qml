
import Qt 4.7

Rectangle {
    width: 200; height: 160

    Text {
        x: progressBar.x; y: 20
        width: progressBar.width
        font.pixelSize: 8
        text: downloader.filename
        elide: Text.ElideRight
    }

    MyProgressBar {
        id: progressBar
        x: 20; y: 60
        width: parent.width-40
        progress: downloader.progress
        size: downloader.size
    }

    Rectangle {
        anchors.left: progressBar.left
        anchors.right: progressBar.right

        color: "#aad"
        y: progressBar.y + progressBar.height + 20
        height: 40

        Text {
            anchors.fill: parent
            color: "#003"
            text: downloader.running?"Please wait...":"Start download"

            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }

        MouseArea {
            anchors.fill: parent
            onClicked: { downloader.start_download() }
        }
    }
}

