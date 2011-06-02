
import Qt 4.7
import com.meego 1.0

PageStackWindow {
    id: pageStack
    anchors.fill: parent
    showToolBar: false
    showStatusBar: false

    initialPage: Page {
        id: mainPage

        TextField {
            id: input
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.right: parent.right

            function handle() {
                python.evaluate(input.text)
                output.text = python.output
                input.text = ''
                input.forceActiveFocus()
            }

            Keys.onReturnPressed: handle()
            Keys.onEnterPressed: handle()

            inputMethodHints: Qt.ImhNoAutoUppercase
        }

        Flickable {
            contentWidth: output.width
            contentHeight: output.height
            clip: true

            anchors {
                top: input.bottom
                left: parent.left
                right: parent.right
                bottom: parent.bottom
            }

            TextArea {
                id: output
                width: mainPage.width
                readOnly: true
            }
        }
    }
}

