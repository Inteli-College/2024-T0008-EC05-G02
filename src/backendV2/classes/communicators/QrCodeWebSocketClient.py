
import websockets
import json

class QrCodeWebSocketClient:
    _self = None
    def __new__(cls,*args,**kwargs):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self
    def __init__(self, uri):
        self.uri = uri

    async def connect(self):
        self.connection = await websockets.connect(self.uri) # type: ignore
        print(f"QRCode Connected to WebSocket server at {self.uri}")

    async def send_message(self, message):
        await self.connection.send(json.dumps(message))

    async def close(self):
        await self.connection.close()