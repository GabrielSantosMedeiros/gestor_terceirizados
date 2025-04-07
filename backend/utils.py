from PySide6.QtCore import QObject

def singleton(cls):
    instances = {}
    def getInstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getInstance


def findComponent(current:QObject, targetName:str):
    
    if current.objectName() == targetName:
        return current
    
    for child in current.children():
        result = findComponent(child, targetName)
        if result:
            return result
