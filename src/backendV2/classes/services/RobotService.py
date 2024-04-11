from typing import Any
import pydobot
from pydobot import Dobot
import serial
import serial.tools.list_ports 
import asyncio

from utils.layout import return_layout_by_id, find_medication_position
from classes.wrappers.QrCodeWrapper import QrCodeWrapper

class InteliArm(Dobot):
    def __init__(self, port=None, verbose=False):
        super().__init__(port=port, verbose=verbose)
    
    def movej_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVJ_XYZ, wait=wait)

    def move_to(self, x, y, z, r, wait=True):
        super()._set_ptp_cmd(x, y, z, r, mode=pydobot.enums.PTPMode.MOVL_XYZ, wait=wait)
class RobotService:
    def __new__(cls):
        cls._self = None
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    

    def __init__(self):
        print('RobotService instantiated')
        self.robot: InteliArm | None = self.init_robot_connection()
        self.robot.r = self.robot.pose()[3]
        self.robot.speed(40,0)
        self.qr = QrCodeWrapper()


    def init_robot_connection(self):
        try:
            ports = serial.tools.list_ports.comports()
            dobot_port: str | None = None
            for port_info in ports:
                print(f"Checking port: {port_info.device}, HWID: {port_info.hwid}")
                if "USB VID:PID=0483:5750 SER=6 LOCATION=1-1:x.0" in port_info.hwid:
                    dobot_port = port_info.device
                    print(f"Dobot encontrado na porta: {dobot_port}")
                    return InteliArm(port=dobot_port)
            print("Nenhum Dobot encontrado")
        except Exception as e:
            print(f"Erro ao conectar com o Dobot: {e}")
            return None
    
    async def bipar_layout(self,layout_id):
        layout: Any | None = return_layout_by_id(layout_id)
        if not layout:
            print(f"Layout {layout_id} not found.")
            return
        await self.process_medications_recursively(layout['remedios'])
    async def beep(self):
        self.robot.movej_to(239.82315063476562, -196.86936950683594, 145, 45, wait=True)
    async def move_robot_to_position(self,position):
        print('robot moving to position ', position)
        self.robot.suck(False)
        safe = 187.95196533203125, -151.02200317382812, 140.7934112548828
        self.robot.movej_to(safe[0],safe[1],safe[2],self.robot.r,wait=True) # safe
        self.robot.suck(True)
        self.robot.movej_to(position['x'],position['y'],position['z'],self.robot.r,wait=True) #pega remedio
        self.robot.movej_to(position['x'],position['y'],position['z']+50,self.robot.r,wait=True)#sobe remedio
        self.robot.movej_to(safe[0],safe[1],safe[2],self.robot.r,wait=True)#safe
        self.robot.movej_to(safe[0],safe[1],safe[2],30,wait=True)#gira remedio pra bipar
    async def process_medications_recursively(self,medications):
        if not medications:
            print("All medications have been processed.")
            return

        # Get the first medication and its position from the stock
        medication = medications[0]
        position = find_medication_position(medication['Nome'])
        
        if position:
            # Move robot arm to medication's position and get the medication
            await self.move_robot_to_position(position)

            # ...
            info = {
                'Nome': medication['Nome'], 
                'Dosagem': medication['Dosagem']
            }

            # Move to QR code reader's position (beep position) and read QR code
            #qr_result, qr_data = await self.qr.handle_action(action='read_qr_code',expected_medication=info)
            
            # Process the QR code result and move medication accordingly
            #await self.process_qr_result(qr_result, qr_data)
            # ...

            # Recursively process the remaining medications
            await self.process_medications_recursively(medications[1:])

if __name__ == '__main__':
    robot = RobotService()
    asyncio.run(robot.bipar_layout('layout_01'))