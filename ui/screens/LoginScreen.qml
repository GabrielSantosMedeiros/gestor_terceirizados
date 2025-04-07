import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: loginScreen
    anchors.centerIn: parent

    Rectangle {
        id: formContainer
        anchors.centerIn: parent
        width: 683
        height: 384
        color: '#F0F0F0'
        radius: 15

        TextField {
            id: emailField
            objectName: 'emailField'
            anchors.horizontalCenter: parent.horizontalCenter
            y: 120
            width: parent.width * 0.8
            font.pixelSize: 24
            font.family: 'Arial'
            placeholderText: 'Email'
        }

        TextField {
            id: passwordField
            objectName: 'passwordField'
            anchors.horizontalCenter: parent.horizontalCenter
            y: 195
            width: parent.width * 0.8
            font.pixelSize: 24
            font.family: 'Arial'
            placeholderText: 'Senha'
            echoMode: TextInput.Password
        } 

        Button {
            id: signInButton
            objectName: 'signInButton'
            anchors.horizontalCenter: parent.horizontalCenter
            y: 275
            width: 120
            height: 45
            text: 'Entrar'
            font.pixelSize: 20
            font.family: 'Arial'
            font.bold: true

            onClicked: {
                screenController.signInEvent()
            }
        }
    }
}
