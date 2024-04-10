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

    async def handle_action(self, action):
        # Handle the action received from the WebSocket server
        if action == 'bipar_layout':
            print("Action called: bipar_layout")
            # Call the Robot service action
            #await self.robot.bipar_layout(data)
        else:
            print(f"Unknown action: {action}")
            return 'Unknown action'
