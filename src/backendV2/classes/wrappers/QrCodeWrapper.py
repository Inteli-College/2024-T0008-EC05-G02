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
       self.ws_client = QrCodeWebSocketClient('ws://localhost:5000')


    async def handle_action(self, action,expected_medication: dict):
        # Handle the action received from the WebSocket server
        if action == 'read_qr_code':
            print("Action called: QRCodeReading")
            await self.ws_client.connect()
            # Call the QR code reader service
            qr_data = await self.qr_reader.read_qr_code(expected_medication) #type: ignore
            print(f"QR DATA OBJECT:{qr_data}")

            #ws.send(qrdata)
            await self.ws_client.send_message({'target': 'Frontend', 'data': qr_data})
            return qr_data
            # Close the WebSocket connection
            #await self.ws_client.close()
        else:
            print(f"Unknown action: {action}")
            return 'Unknown action'