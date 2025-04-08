import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: menuView

    Column {
        anchors.centerIn: parent
        spacing: 20

        Button {
            id: menuDashboard
            text: 'Dashboard'
            font.pixelSize: 16
            font.family: 'Arial'
            width: 120
            height: 45

            onClicked: {
                homeController.activateContent('DASHBOARD')
            }
        }
        Button {
            id: menuEmpresas
            text: 'Empresas'
            font.pixelSize: 16
            font.family: 'Arial'
            width: 120
            height: 45

            onClicked: {
                homeController.activateContent('EMPRESAS')
            }
        }
        Button {
            id: menuVeiculos
            text: 'Veiculos'
            font.pixelSize: 16
            font.family: 'Arial'
            width: 120
            height: 45

            onClicked: {
                homeController.activateContent('VEICULOS')
            }
        }
        Button {
            id: menuFuncionarios
            text: 'Funcionarios'
            font.pixelSize: 16
            font.family: 'Arial'
            width: 120
            height: 45

            onClicked: {
                homeController.activateContent('FUNCIONARIOS')
            }
        }
        Button {
            id: menuConfig
            text: 'Configurações'
            font.pixelSize: 16
            font.family: 'Arial'
            width: 120
            height: 45

            onClicked: {
                homeController.activateContent('CONFIGURAÇÕES')
            }
        }
    }
}