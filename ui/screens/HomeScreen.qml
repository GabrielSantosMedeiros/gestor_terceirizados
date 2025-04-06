import QtQuick 2.15
import QtQuick.Controls 2.15
import '../views'

Rectangle {
    id: homeScreen
    anchors.fill: parent
    color: '#E0E0E0'

    MenuView {
        x: 10
        y: 10
        width: 200
        height: 673
        color: '#F0F0F0'
        radius: 15
    }

    HeaderView {
        x: 227
        y: 10
        width: 1125
        height: 175
        color: '#F0F0F0'
        radius: 15
    }
}