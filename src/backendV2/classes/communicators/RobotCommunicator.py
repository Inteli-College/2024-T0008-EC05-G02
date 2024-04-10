import os
import websockets
import asyncio
import serial
from serial.tools import list_ports
from classes.services.RobotService import RobotService
class RobotCommunicator:
    _self = None
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    
    def __init__(self):
        print('Robot Communicator Initialized')
        self.serial_port = self.find_pico_port()
        self.serial_connection = serial.Serial(self.serial_port, baudrate=115200, timeout=1)

    def find_pico_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.vid == 0x2E8A and port.pid == 0x0005:  # Raspberry Pi Pico VID and PID
                print(f"Pico found on port: {port.device}")
                return port.device
        print(f"Device not found on any port")
        return None
    async def listen_to_serial(self):
        print('Listening to serial port')
        while True:
            if self.serial_connection.in_waiting > 0:
                serial_data = self.serial_connection.readline().decode('utf-8').rstrip()
                print(f"Data from Pico: {serial_data}")
                # Process the data from Pico

    async def start(self):
        # Create tasks for WebSocket and serial communication
        await self.listen_to_serial()