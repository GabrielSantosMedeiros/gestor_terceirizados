from PySide6.QtCore import Slot, QObject, QMetaObject, Qt
from backend.utils import findComponent
from backend.core import Engine

class ScreenController(QObject):

    def __init__(self):
        super().__init__()
        self.engine = Engine()


    @Slot()
    def signInEvent(self):
        root = self.engine.rootObjects()[0]
        email = findComponent(root, 'emailField')
        password = findComponent(root, 'passwordField')