import asyncio 
from classes.services.RobotService import RobotService
from classes.wrappers.QrCodeWrapper import QrCodeWrapper
#from classes.communicators.RobotCommunicator import RobotCommunicator
class RobotWrapper():
    _self = None
    def __new__(cls,*args,**kwargs):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
        
    def __init__(self):
        print('RobotWrapper instantiated')
        self.qr = QrCodeWrapper()
        self.robot = RobotService()
        print('RobotService instantiated')

