import QtQuick
import QtQuick.Controls
import 'screens'


ApplicationWindow {
    visible: true
    visibility: Window.Maximized
    color: '#E0E0E0'

    StackView {
        id: screenStack
        anchors.fill: parent
        initialItem: LoginScreen {}
    }
}
