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
    def activateContent(self, content:str):
        header_title = findComponent(self.engine.rootObjects()[0], 'headerTitle')
        dashboardGeneralInfo = findComponent(self.engine.rootObjects()[0], 'dashboardGeneralinformationComponent')
        dashboardPreview = findComponent(self.engine.rootObjects()[0], 'dashboardPreviewComponent')
        dashboardGraph = findComponent(self.engine.rootObjects()[0], 'dashboardGraphicComponent')

        match content:
            
            case 'DASHBOARD':
                header_title.setProperty('text', content)
                dashboardGeneralInfo.setProperty('visible', True)
                dashboardPreview.setProperty('visible', True)
                dashboardGraph.setProperty('visible', True)
            
            case 'EMPRESAS':
                header_title.setProperty('text', content)
                dashboardGeneralInfo.setProperty('visible', False)
                dashboardPreview.setProperty('visible', False)
                dashboardGraph.setProperty('visible', False)
            
            case 'VEICULOS':
                header_title.setProperty('text', content)
                dashboardGeneralInfo.setProperty('visible', False)
                dashboardPreview.setProperty('visible', False)
                dashboardGraph.setProperty('visible', False)

            case 'FUNCIONARIOS':
                header_title.setProperty('text', content)
                dashboardGeneralInfo.setProperty('visible', False)
                dashboardPreview.setProperty('visible', False)
                dashboardGraph.setProperty('visible', False)

            case 'CONFIGURAÇÕES':
                header_title.setProperty('text', content)
                dashboardGeneralInfo.setProperty('visible', False)
                dashboardPreview.setProperty('visible', False)
                dashboardGraph.setProperty('visible', False)


