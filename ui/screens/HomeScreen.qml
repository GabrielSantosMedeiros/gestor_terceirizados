import QtQuick 2.15
import QtQuick.Controls 2.15
import '../views'

Rectangle {
    id: homeScreen
    anchors.fill: parent
    color: '#E0E0E0'

    MenuView {
        anchors.left: parent.left
        width: 200
        height: parent.height
        color: '#F0F0F0'
    }
}