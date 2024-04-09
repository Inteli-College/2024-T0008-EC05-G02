import os
import websockets
import asyncio
import serial
from serial.tools import list_ports
from classes.services.RobotService import RobotService
class RobotCommunicator:

    def __new__(cls):
        cls._self = None
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    
    def __init__(self):
        print('RobotWebSocketHandler instantiated')
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
    
    async def listen_to_websocket(self):
        async with websockets.connect(self.websocket_url) as ws:
            while True:
                message = await ws.recv()
                print(f"Message from WebSocket: {message}")
                # Process the message and potentially send data to Pico
    async def listen_to_serial(self):
        while True:
            if self.serial_connection.in_waiting > 0:
                serial_data = self.serial_connection.readline().decode('utf-8').rstrip()
                print(f"Data from Pico: {serial_data}")
                # Process the data from Pico

    async def start(self):
        # Create tasks for WebSocket and serial communication
        websocket_task = asyncio.create_task(self.listen_to_websocket())
        serial_task = asyncio.create_task(self.listen_to_serial())

        # Run both tasks concurrently
        await asyncio.gather(websocket_task, serial_task)
