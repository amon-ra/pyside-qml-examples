
import Qt 4.7

Rectangle {
    width: 400
    height: 400
    color: C.Colors.Background

    Repeater {
        model: C.Items.Count

        Text {
            y: index * C.Step.Y
            x: index * C.Step.X
            anchors {
                margins: C.Border
            }
            color: C.Colors.Foreground
            font.bold: C.BoldText
            text: C.CustomText + C.Items.Suffixes[index]
        }
    }
}

