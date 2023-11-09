import json
import xml.etree.ElementTree as ET
import ssl
import websockets

from game import Game
from dictionarys import houses,colors

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
                        print(f"House name: {house_name}")
                        game.list_house_information(house_name)
                    else:
                        # todo responder por voz que não foi encontrado
                        print("No house found")
                else:
                    # todo responder por voz que não foi encontrado
                    print("No house found")
            else:
                # todo responder por voz que não foi encontrado
                print("No house found")
        elif intent == "choose_color":
            if message["entities"]:
                if len(message["entities"]) > 0:
                    color_name = message["entities"][0]["value"].lower()
                    if color_name in colors:
                        color_name = colors[color_name]
                        print(f"Color name: {color_name}")
                        game.choose_color(color_name)
                    else:
                        # todo responder por voz que não foi encontrado
                        print("No color found")
                else:
                    # todo responder por voz que não foi encontrado
                    print("No color found")
            else:
                # todo responder por voz que não foi encontrado
                print("No color found")
        elif intent == "roll_dice":
            print("Roll dice")
            game.roll_dice()
        elif intent == "end_turn":
            print("End turn")
            game.end_turn()
        elif intent == "buy_house":
            print("buy_house")
            game.buy()
        elif intent == "join_game":
            print("join_game")
            game.join_game_after_color()
        elif intent == "start_game":
            print("start_game")
            game.start_game()
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
    
    async with websockets.connect(mmi_cli_out_add, ssl=ssl_context) as websocket:
        print("Connected to MMI CLI OUT")
                
        while True:
            try:
                msg = await websocket.recv()
                await message_handler(game=game, message=msg)
            except Exception as e:
                print(f"Error: {e}")

    game.close()
    system.exit(0)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())