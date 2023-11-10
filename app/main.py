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
intent_before = None

async def message_handler(game: Game, message:str):
    global intent_before
    message = process_message(message)
    # print(f"Message received: {message}")
    if message == "OK":
        return "OK"
    elif message["intent"]["name"]:
        print(f"Message received/ intent: {message['intent']['name']}")
        intent = message["intent"]["name"]
        if intent == "insert_name":
            # TODO IMPLEMENTAR
            print("Insert name")
            intent_before = intent
        elif intent == "create_game":
            game.create_game()
            intent_before = intent
        elif intent == "choose_color":
            intent_before = intent
            if message["entities"]:
                if len(message["entities"]) > 0:
                    color_name = message["entities"][0]["value"].lower()
                    if color_name in colors:
                        color_name = colors[color_name]
                        print(f"Color name: {color_name}")
                        game.choose_color(color_name)
                    else:
                        print("Não foi encontrada a cor")
                        game.tts("Não foi encontrada a cor")
                else:
                    print("Não foi encontrada a cor 2")
                    game.tts("Não foi encontrada a cor")
            else:
                game.tts("Não foi encontrada a cor")
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
                        game.tts("Não foi encontrada a propriedade")
                else:
                    game.tts("Não foi encontrada a propriedade")
            else:
                game.tts("Não foi encontrada a propriedade")
        elif intent == "start_game":
            game.start_game()
            intent_before = intent
        elif intent == "roll_dice":
            game.roll_dice()
            intent_before = intent
        elif intent == "end_turn":
            game.end_turn()
            intent_before = intent
        elif intent == "buy_house":
            game.buy()
            intent_before = intent
        elif intent == "leave_prison":
            game.leave_prison()
            intent_before = intent
        elif intent == "give_up_game":
            print("give_up_game")
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
        
        print("Closing connection")
        await websocket.close()
        print("Connection closed")
        exit(0)
    


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())