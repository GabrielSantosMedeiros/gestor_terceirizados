from PySide6.QtCore import Slot, QObject, QMetaObject, Qt
from backend.utils import findComponent
from backend.core import Engine

class ScreenController(QObject):

    def __init__(self):
        super().__init__()
        self.engine = Engine()


    @Slot()
    def signInEvent(self):
        print('ola')


class HomeController(QObject):
    
    def __init__(self):
        super().__init__()
        self.engine = Engine()
    

    @Slot(str)
    def changeHeaderTitle(self, new_title:str):
        header_title = findComponent(self.engine.rootObjects()[0], 'headerTitle')
        header_title.setProperty('text', new_title)
    