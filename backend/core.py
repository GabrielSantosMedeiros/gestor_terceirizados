from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


__APPLICATION = QGuiApplication([])

__QML_ENGINE = QQmlApplicationEngine()


def Application():
    return __APPLICATION

def Engine():
    return __QML_ENGINE 
