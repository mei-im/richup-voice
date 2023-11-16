import json
from os import system
import xml.etree.ElementTree as ET
import ssl
import websockets
from utils import *


from game import Game
from dictionarys import houses,colors
from tts import TTS

HOST = "127.0.0.1"
not_quit = True
intent_before = None
list_intent = ["insert_name", "create_game", "choose_color", "information_house", "start_game", "roll_dice", "end_turn", "buy_house", "leave_prison", "give_up_game", "close_game", "help"]


async def message_handler(game: Game, message:str):
    global intent_before
    message = process_message(message)
    # print(f"Message received: {message}")
    if message == "OK":
        return "OK"
    elif message["intent"]["name"] in list_intent:
        print(f"Message received/ intent: {message['intent']['name']}")
        intent = message["intent"]["name"]
        if message["intent"]["confidence"] < 0.8:
            game.tts(random_not_understand())
        elif intent == "insert_name":#DONE  
            if message["entities"]:
                if len(message["entities"]) > 0:
                    name = message["entities"][0]["value"].lower()
                    game.insert_name(name)
                else:
                    game.tts(random_not_understand_name())
            else:
                game.tts(random_not_understand_name())
            intent_before = intent
        elif intent == "create_game": # TODO VERIFICAR SE ESTÁ A FUNCIONAR
            game.create_game()
            intent_before = intent
        elif intent == "choose_color": # DONE
            intent_before = intent
            if message["entities"]:
                if len(message["entities"]) > 0:
                    color_name = message["entities"][0]["value"].lower()
                    if color_name in colors:
                        color_name = colors[color_name]
                        print(f"Color name: {color_name}")
                        game.choose_color(color_name)
                    else:
                        game.tts("Escolhe uma cor válida")
                else:
                    game.tts("Por favor, repita o nome da cor")
            else:
                game.tts("Por favor, diga o nome da cor")
        elif intent == "information_house":
            intent_before = intent
            if message["entities"]:
                if len(message["entities"]) > 0:
                    house_name = message["entities"][0]["value"].lower()
                    if house_name in houses:
                        house_name = houses[house_name]
                        print(f"House name: {house_name}")
                        game.list_house_information(house_name)
                    else:
                        game.tts("O jogo não tem essa propriedade")
                else:
                    game.tts("Por favor, repita o nome da propriedade")
            else:
                game.tts("Por favor, diz o nome da propriedade")
        elif intent == "start_game":
            game.start_game()
            intent_before = intent
        elif intent == "roll_dice": # DONE
            game.roll_dice()
            intent_before = intent
        elif intent == "end_turn": # DONE
            game.end_turn()
            intent_before = intent
        elif intent == "buy_house":
            game.buy()
            intent_before = intent
        elif intent == "leave_prison":
            game.leave_prison()
            intent_before = intent
        elif intent == "give_up_game":
            game.give_up_game()
            intent_before = intent
        elif intent_before == "give_up_game" and intent == "confirm":
            game.confirm_give_up_game()
            game.tts("Desististe do jogo. Obrigado por jogar Richup.")
            game.tts("Podes fechar o jogo, ou continuar a ver o jogo a decorrer.")
            intent_before = intent
        elif intent_before == "give_up_game" and intent == "deny":
            game.cancel_give_up_game()
            game.tts("Ainda bem que não desististe. Continua a jogar.")
            intent_before = intent
        elif intent == "close_game":
            game.tts("Obrigado por jogar Richup")
            game.close()
            global not_quit
            not_quit = False

        elif intent == "help":
            print("help")
            # TODO IMPLEMENTAR
        else:      
            game.tts(random_not_understand())
            print(f"Command not found: {message}")
    else:
        game.tts(random_not_understand())
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
                tts("Ocorreu um erro, a fechar o jogo")
                print(f"Error: {e}")
        
        print("Closing connection")
        await websocket.close()
        print("Connection closed")
        exit(0)
    


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())