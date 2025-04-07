import QtQuick 2.15
import '../views'
import '../views/components'

Rectangle {
    id: homeScreen
    objectName: 'homeScreen'
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

    HeaderComponent {
        x: 227
        y: 10
        width: 1125
        height: 175
        color: '#F0F0F0'
        radius: 15
    }

    DashboardGeneralInformationComponent {
        x: 227
        y: 200
        width: 658
        height: 270
        color: '#F0F0F0'
        radius: 15
    }

    DashboardPreviewComponent {
        x: 897
        y: 200
        width: 455
        height: 484
        color: '#F0F0F0'
        radius: 15
    }

    DashboardGraphicComponent {
        x: 227
        y: 525
        width: 657
        height: 158
        color: '#F0F0F0'
        radius: 15
    }
}