import asyncio
import json
from classes.services.QrCodeService import QRCodeService

class QrCodeWrapper:
    _self = None
    
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
       self.qr_reader = QRCodeService()


    async def handle_action(self, action, data):
        # Handle the action received from the WebSocket server
        if action == 'read_qr_code':
            print("Action called: QRCodeReading")
            # Call the QR code reader service
            qrdata = await self.qr_reader.read_qr_code('Agua Destilada')
            print(qrdata)
            #ws.send(qrdata)
        else:
            print(f"Unknown action: {action}")
            return 'Unknown action'