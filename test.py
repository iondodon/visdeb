import asyncio
import websockets
import time
import json

async def algo(websocket):
  data = [9, 8, 7, 6, 4, 3, 2, 1]
  p5_structure = []

  for i in range(len(data)):
    p5_new_element = {
      "elementType": "rect",
      "x": i * 60,
      "y": 50,
      "w": 50,
      "color": [255, 255, 255],
      "children": [],
    }
    p5_text = {
      "elementType": "text",
      "text": str(data[i]),
      "x": i * 60 + 25,
      "y": 70,
      "x2": 100,
      "y2": 100,
      "color": [0, 0, 0],
      "children": [],
    }
    p5_new_element["children"].append(p5_text)
    p5_structure.append(p5_new_element)
    p5_request = {
      "type": "request",
      "command": "update",
      "payload": p5_structure,
      "timestamp": time.time()
    }
    await websocket.send(json.dumps(p5_request))
    p5_response = await websocket.recv()
    print(p5_response)

    time.sleep(1)

  for i in range(len(data)):
    for j in range(len(data) - 1):
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
        time.sleep(1)

async def run(websocket, path):
  await algo(websocket)

start_server = websockets.serve(run, "localhost", 1234)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
