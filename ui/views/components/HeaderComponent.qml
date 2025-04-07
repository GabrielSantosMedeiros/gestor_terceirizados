import QtQuick 2.15

Rectangle {
    id: headerComponent

    Text {
        id: headerTitle
        objectName: 'headerTitle'
        x: 50
        y: 70
        text: 'DASHBOARD'
        font.pixelSize: 24
        font.family: 'Arial'
        font.bold: true
    }
}
