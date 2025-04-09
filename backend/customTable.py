from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from typing import *


class CustomTable(QAbstractTableModel):
    
    def __init__(self, data:List[Dict[str, Any]], headers:List[str]):
        super().__init__()
        self.data = data
        self.headers = headers


    def rowCount(self, parent = QModelIndex()):
        return len(self.data)

    
    def columnCount(self, parent = QModelIndex()):
        return len(self.headers)
    

    def data(self, row, column, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.data[row][column]
        return None
    