from PySide6.QtGui import QGuiApplication
from backend.utils import getQmlEngine
import sys


if __name__ == '__main__':
    
    app = QGuiApplication([])

    engine = getQmlEngine()
    engine.load('ui/main.qml')

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())