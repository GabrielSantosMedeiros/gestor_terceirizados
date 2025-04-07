import QtQuick 2.15
import QtQuick.Controls 2.15
import 'screens'


ApplicationWindow {
    visible: true
    visibility: Window.Maximized
    color: '#E0E0E0'

    StackView {
        id: screenStack
        objectName: 'screenStack'
        anchors.fill: parent
        initialItem: LoginScreen {}
    }
}
