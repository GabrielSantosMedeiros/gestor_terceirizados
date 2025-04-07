from PySide6.QtGui import QGuiApplication
from backend.core import Application, Engine
from backend.controllers import ScreenController, HomeController
import sys


if __name__ == '__main__':
    
    app = Application()

    engine = Engine()
    engine.load('ui/main.qml')

    screenController = ScreenController()
    engine.rootContext().setContextProperty('screenController', screenController)

    homeController = HomeController()
    engine.rootContext().setContextProperty('homeController', homeController)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())