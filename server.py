import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print("msg Income:",message)
        await websocket.send(message+"DONE~")

async def main():
    async with serve(echo, "172.16.110.118", 8765):
        await asyncio.Future()  # run forever

try:
    asyncio.run(main())
except:
    print("hold")