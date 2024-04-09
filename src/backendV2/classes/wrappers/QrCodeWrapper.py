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


    async def handle_action(self, action, data):
        # Handle the action received from the WebSocket server
        if action == 'read_qr_code':
            print("Action called: QRCodeReading")
            await self.ws_client.connect()
            # Call the QR code reader service
            qr_data = await self.qr_reader.read_qr_code('Agua Destilada')
            print(qr_data)
            #ws.send(qrdata)
            await self.ws_client.send_message({'target': 'Frontend', 'data': qr_data})
            # Close the WebSocket connection
            #await self.ws_client.close()
        else:
            print(f"Unknown action: {action}")
            return 'Unknown action'