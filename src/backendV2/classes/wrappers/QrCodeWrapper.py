import asyncio
import json
from classes.services.QrCodeService import QRCodeService
from classes.communicators.QrCodeWebSocketClient import QrCodeWebSocketClient
class QrCodeWrapper:
    _self = None
    
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
       
       self.qr_reader = QRCodeService()
       self.ws_client = QrCodeWebSocketClient('ws://localhost:3000')

    async def beep(self,target):
        await self.ws_client.connect()
        qr_data = await self.qr_reader.read_qr_code(target)
        await self.ws_client.send_message({'target': 'Frontend', 'data': qr_data})
        await self.ws_client.close()
        return qr_data

    