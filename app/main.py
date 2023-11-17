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
intent_before = ""
list_intent = ["insert_name", "create_room", "choose_color", "information_house", "start_game", "roll_dice", "end_turn", "buy_house", "leave_prison", "give_up_game", "confirm", "deny", "close_game",
               "list_of_colors", "game_info", "help", "mute", "unmute"]

GAME_INFO = """O RichUp é a adaptação do clássico jogo de tabuleiro que combina estratégia e negociação. 
            Cada jogador começa com dinheiro e escolhe uma cor para representá-lo no tabuleiro. 
            O objetivo é adquirir propriedades, construir casas e hotéis, e cobrar aluguer dos adversários.
            Durante o jogo, os jogadores negociam entre si, podem comprar, vender e trocar propriedades. 
            O vencedor é o último jogador que não vai à falência. Para ganhar, é essencial tomar decisões financeiras inteligentes, formar alianças e gerir recursos com sabedoria. 
            Boa sorte!"""


async def message_handler(game: Game, message:str):
    global intent_before
    message = process_message(message)
    # print(f"Message received: {message}")
    if message == "OK":
        return "OK"
    elif message["intent"]["name"] in list_intent:
        print(f"Message received/ intent: {message['intent']['name']}")
        intent = message["intent"]["name"]
        if message["intent"]["confidence"] < 0.7:
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
        elif intent == "create_room": # DONE
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
                        game.tts(random_not_valid_color())
                else:
                    game.tts(random_not_understand_color())
            else:
                game.tts(random_not_understand_color())
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
        elif intent == "start_game": #DONE
            game.start_game()
            intent_before = intent
        elif intent == "roll_dice": #DONE
            game.roll_dice()
            intent_before = intent
        elif intent == "end_turn": #Done
            game.end_turn()
            intent_before = intent
        elif intent == "buy_house": #DONE
            game.buy()
            intent_before = intent
        elif intent == "leave_prison":
            game.leave_prison()
            intent_before = intent
        elif intent == "give_up_game": #DONE
            game.give_up_game()
            intent_before = intent
        elif  intent == "confirm" and "give_up_game" in intent_before: #DONE
            game.confirm_give_up_game()
            game.tts("Podes fechar o jogo, ou continuar a ver o jogo a decorrer.")
            intent_before = intent
        elif  intent == "deny" and "give_up_game" in intent_before: #DONE
            game.cancel_give_up_game()
            intent_before = intent
        elif intent == "close_game":#DONE
            game.tts("Obrigado por jogar Richup")
            game.close()
            global not_quit
            not_quit = False
        elif intent == "list_of_colors": #DONE
            colors_in_pt =["verde lima", "amarela", "laranja", "vermelho", "azul", "ciano", "verde", "castanha", "magenta", "cor de rosa"]
            string_colors = ", ".join(colors_in_pt)
            game.tts(f"As cores disponíveis são: {string_colors}")
            intent_before = intent
        elif intent == "game_info": # DONE
            game.tts(GAME_INFO)
            intent_before = intent
        elif intent == "mute": # DONE
            game.mute_func()
            intent_before = intent
        elif intent == "unmute": # DONE
            game.unmute()
            intent_before = intent
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