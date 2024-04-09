import asyncio 
from classes.services.RobotService import RobotService

class RobotWrapper():
    def __new__(cls):
        cls._self = None
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    def __init__(self):
        print('RobotWrapper instantiated')
        self.robot = RobotService()
        print('RobotWrapper instantiated')