from typing import Any
from pydobot import Dobot
import serial
import serial.tools.list_ports 


from utils.layout import return_layout_by_id
from classes.wrappers.QrCodeWrapper import QrCodeWrapper


class RobotService:
    def __new__(cls):
        cls._self = None
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    

    def __init__(self):
        print('RobotService instantiated')
        self.robot: Dobot | None = self.init_robot_connection()
        self.qr = QrCodeWrapper


    def init_robot_connection(self):
        try:
            ports = serial.tools.list_ports.comports()
            dobot_port: str | None = None
            for port_info in ports:
                print(f"Checking port: {port_info.device}, HWID: {port_info.hwid}")
                if "USB VID:PID=0483:5750 SER=6 LOCATION=1-1:x.0" in port_info.hwid:
                    dobot_port = port_info.device
                    print(f"Dobot encontrado na porta: {dobot_port}")
                    return Dobot(port=dobot_port)
            print("Nenhum Dobot encontrado")
        except Exception as e:
            print(f"Erro ao conectar com o Dobot: {e}")
            return None
    

    def bipar_layout(self,layout_id):
        layout: Any | None = return_layout_by_id(layout_id)