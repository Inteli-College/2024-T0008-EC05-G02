from pydobot import Dobot
import serial
import serial.tools.list_ports
from classes.wrappers.QrCodeWrapper import QrCodeWrapper
from utils.layout import *
class RobotService:
    def __new__(cls):
        cls._self = None
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    

    def __init__(self):
        print('RobotService instantiated')
        #self.robot = self.init_robot_connection()
        self.robot = self.init_robot_connection()
        self.qr = QrCodeWrapper()


    def init_robot_connection(self):
        print('init_robot_connection')
        ports = list(serial.tools.list_ports.comports())
        for port_info in ports:
            print(port_info.device)
            try:
                print('Trying to connect to Dobot')
                conn = Dobot(port=port_info.device, verbose=False)
                print('Connected to Dobot')
                return conn  # Return the connection object upon success
            except (serial.serialutil.SerialException, OSError) as e:
                print(f"Connection attempt failed: {e}")
                # You may want to log this error or handle it accordingly.
        print("No Dobot found on any port.")
        return None
    

    def bipar_layout(layout_id):
        pass