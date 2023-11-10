import json
from os import system
import xml.etree.ElementTree as ET
import ssl
import websockets


from game import Game
from dictionarys import houses,colors
from tts import TTS

HOST = "127.0.0.1"
not_quit = True

async def message_handler(game: Game, message:str):
    message = process_message(message)
    print(f"Message received: {message}")

    if message == "OK":
        return "OK"
    elif message["intent"]["name"]:
        intent = message["intent"]["name"]
        if intent == "insert_name":
            print("Insert name")
        elif intent == "create_game":
            print("Create game")
        elif intent == "choose_color":
            if message["entities"]:
                if len(message["entities"]) > 0:
                    color_name = message["entities"][0]["value"].lower()
                    if color_name in colors:
                        color_name = colors[color_name]
                        game.choose_color(color_name)
                    else:
                        game.tts("Não foi encontrada a cor")
                else:
                    game.tts("Não foi encontrada a cor")
            else:
                game.tts("Não foi encontrada a cor")
        elif intent == "information_house":
            if message["entities"]:
                if len(message["entities"]) > 0:
                    house_name = message["entities"][0]["value"].lower()
                    if house_name in houses:
                        house_name = houses[house_name]
                        game.list_house_information(house_name)
                    else:
                        game.tts("Não foi encontrada a propriedade")
                else:
                    game.tts("Não foi encontrada a propriedade")
            else:
                game.tts("Não foi encontrada a propriedade")
        elif intent == "start_game":
            game.start_game()
        elif intent == "roll_dice":
            game.roll_dice()
        elif intent == "end_turn":
            game.end_turn()
        elif intent == "buy_house":
            game.buy()
        elif intent == "leave_prison":
            print("leave_prison")
            # TODO IMPLEMENTAR
        elif intent == "give_up_game":
            print("give_up_game")
            # TODO IMPLEMENTAR
        elif intent == "close_game":
            print("close_game")
            game.close()
            game.tss("Obrigado por jogar Richup")
            global not_quit
            not_quit = False

        elif intent == "help":
            print("help")
            # TODO IMPLEMENTAR
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
    
    tts = TTS(FusionAdd=f"https://{HOST}:8000/IM/USER1/APPSPEECH").sendToVoice
    game = Game(TTS=tts)
    tts("Bem vindo ao Richup, o jogo de tabuleiro online")

    mmi_cli_out_add = f"wss://{HOST}:8005/IM/USER1/APP"

    #SSL config 
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Connect to websocket
    
    async with websockets.connect(mmi_cli_out_add, ssl=ssl_context) as websocket:
        print("Connected to MMI CLI OUT")
                
        while not_quit:
            try:
                msg = await websocket.recv()
                await message_handler(game=game, message=msg)
            except Exception as e:
                print(f"Error: {e}")
                # terminar ligação por websocket
        
        print("Closing connection")
        await websocket.close()
        print("Connection closed")
        exit(0)
    


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())