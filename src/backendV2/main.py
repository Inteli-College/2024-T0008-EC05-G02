import asyncio
from classes.wrappers.WebSocketWrapper import WebSocketWrapper

async def main():
    # Initialize WebSocketWrapper and QrCodeWrapper
    ws = WebSocketWrapper('localhost', 5000)
    # Schedule both tasks to run concurrently
    websocket_task = asyncio.create_task(ws.start())
    

    # Wait for both tasks to complete (they may run indefinitely)
    await asyncio.gather(websocket_task)

if __name__ == '__main__':
    asyncio.run(main())
