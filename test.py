import asyncio
import websockets
import time
import json

async def algo(websocket):
  for i in range(10):
    command = {
        "command": "addElement",
        "payload": {
            "elementType": "circle",
            "x": 10 * i,
            "y": 10 * i,
            "r": 10
        },
        "timestamp": time.time()
    }

    command_json_string = json.dumps(command)
    await websocket.send(command_json_string)

    await asyncio.sleep(1)
    
    received_data = await websocket.recv()

async def run(websocket, path):
  await algo(websocket)

start_server = websockets.serve(run, "localhost", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
