 
import QtQuick 1.0

Rectangle {
    width: 200
    height: 200

    ListView {
        id: listView
        
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        height: parent.height -20
        
        model: list
        delegate: listDelegate
    }
    
    Component {
        id: listDelegate

        Item {
            height: listDelegateTitle.height + listDelegateText.height
            
            Text {
                id: listDelegateTitle
                
                font.bold: true
                anchors.top: parent.top
                text: model.title
            }
            Text {
                id: listDelegateText
                
                anchors.bottom: parent.bottom
                text: model.text
            }
        }
    }
    
    //add button
    Rectangle {
        anchors.top: listView.bottom
        height: addText.height
        width: addText.width

        MouseArea {
            anchors.fill: parent
            onClicked: list.add()
        }
        
        Text {
            id: addText
            text: 'add'
        }
    }
    
    //remove button
    Rectangle {
        anchors.top: listView.bottom
        anchors.right: parent.right
        height: removeText.height
        width: removeText.width

        MouseArea {
            anchors.fill: parent
            onClicked: list.remove()
        }
        
        Text {
            id: removeText
            text: 'remove'
        }
    }
}
