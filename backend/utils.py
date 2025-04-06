from PySide6.QtQml import QQmlApplicationEngine


def singleton(cls):
    instances = {}
    def getInstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getInstance



@singleton
def getQmlEngine():
    return QQmlApplicationEngine()