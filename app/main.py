import json
import xml.etree.ElementTree as ET
import ssl
import websockets

from game import Game
from dictionarys import houses

HOST = "localhost"

async def message_handler(game: Game, message:str):
    message = process_message(message)
    print(f"Message received: {message}")

    if message == "OK":
        return "OK"
    elif message["intent"]["name"]:
        intent = message["intent"]["name"]
        if intent == "information_house":
            if message["entities"]:
                if len(message["entities"]) > 0:
                    house_name = message["entities"][0]["value"].lower()
                    if house_name in houses:
                        house_name = houses[house_name]
                        print("House found")
                        game.list_house_information(house_name)
                    else:
                        # todo responder por voz que não foi encontrado
                        print("No house found")
                else:
                    # todo responder por voz que não foi encontrado
                    print("No house found")
            # await game.start_game()
        # elif message["intent"]["intentName"] == "roll_dice":
        #     await game.roll_dice()
        # elif message["intent"]["intentName"] == "end_turn":
        #     await game.end_turn()
        # elif message["intent"]["intentName"] == "buy":
        #     await game.buy()
        # elif message["intent"]["intentName"] == "build":
        #     await game.build()
        else:
            print(f"Command not found: {message}")
    else:
        print(f"Command not found: {message}")


def process_message(message):
    if message == "OK":
        return "OK"
    else:
        json_command = ET.fromstring(message).find(".//command").text
        command = json.loads(json_command)["nlu"]
        command = json.loads(command)
        print(f"Command received: {command['text']}")
        return command
    
async def main():
    
    game = Game()

    mmi_cli_out_add = f"wss://{HOST}:8005/IM/USER1/APP"

    #SSL config 
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Connect to websocket
    try:
        async with websockets.connect(mmi_cli_out_add, ssl=ssl_context) as websocket:
            print("Connected to MMI CLI OUT")
            
            while True:
                msg = await websocket.recv()
                await message_handler(game=game, message=msg)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())