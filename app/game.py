import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from utils import random_frase_dados
from mapping import Buttons, Inputs, Houses, Colors
from new_dictonarys import colors_in_pt


class Game:
    def __init__(self, TTS) -> None:
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.tts = TTS
        self.tts("Bem vindo ao Monopoly online, um jogo de tabuleiro para toda a família e amigos")
        self.button = Buttons(self.browser)
        self.input = Inputs(self.browser)
        self.house = Houses(self.browser)
        self.colors = Colors(self.browser)
        time.sleep(4)
        self.button.accept_cookies.click()
        time.sleep(2)
        self.tts("Para começar, podes inserir o teu nome. E criar uma sala para ti e para os teus amigos")


    def join_game(self, name):
        try:
            time.sleep(3)
            self.input.name.send_keys(name)
            self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
            time.sleep(3)
            self.tts("Agora, podes entrar numa sala privada ou pública")
        except:
            self.tts("Não é permitido, mudares o teu nome neste momento")

    def create_game(self):
        try: 
            if self.button.create_private_game:
                self.input.name.send_keys("")
                if self.input.name.get_attribute("value") == "":
                    self.tts("Como não inseriste nenhum nome, vou gerar um para ti")
                    self.button.randomize_name.click()
                    self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
                time.sleep(3)
                self.tts("A criar uma sala")
                self.button.create_private_game.click()
                time.sleep(3)
                self.tts("Escolha a cor com que quer jogar")
            else:
                self.tts("Não é permitido, criares uma sala neste momento")
        except:
            self.tts("Não é permitido, criares uma sala neste momento")

    def list_house_information(self,house_name):
        print("Game : list_house_information")
        house = self.house.__getattribute__(house_name)
        house.click()
        self.tts(f"Já consegues ver a informação da propriedade {house_name}")
        time.sleep(5)
        house.click()
        self.tts("A informação da propriedade foi minimizada")

    # DONE
    def choose_color(self, color):
        try: 
            if self.button.join_game_after_color.text.lower() == 'join game':
                print("join game")
                name_color = colors_in_pt[color]
                color = self.colors.__getattribute__(color)
                color.click()
                self.tts(f"Ficaste com a cor {name_color}")
                time.sleep(3)
                self.tts("Espera que entre na sala")
                time.sleep(3)
                self.button.join_game_after_color.click()
                time.sleep(3)
                self.tts("Bem vindo ao sua sala")
            else:
                self.tts("Não é permitido escolheres a cor, neste momento")
                
        except:
            self.tts("Não é permitido escolheres a cor, enquanto não estás numa sala ou num jogo a decorrer")

    def roll_dice(self):
        try: 
            if self.button.roll_dice.text.lower() == 'roll the dice' or \
                self.button.roll_dice.text.lower() == 'roll again':
                self.button.roll_dice.click()
                self.tts("Os dados foram lançados")
            else:
                self.tts(random_frase_dados())
        except: 
            self.tts("Não é a tua vez de Jogar")

    def end_turn(self):
        try: 
            if self.button.end_turn.text == 'End turn':
                self.button.end_turn.click()
                self.tts("Acabaste a tua ronda")
            else:
                self.tts("Não é a tua vez de acabar a ronda")
        except:
            self.tts("Não é permitido, acabar a ronda neste momento")

    def buy(self):
        try:
            if "Buy" in self.button.buy.text:
                self.button.buy.click()
                self.tts("Adquiriste a propriedade")
            else:
                self.tts("Não podes comprar nenhuma propriedade por agora")
        except:
            self.tts("Não é permitido, comprares alguma propriedade neste momento")

    def start_game(self):
        try:
            if self.button.enable_bots:
                self.button.enable_bots.click()
            time.sleep(3)
            self.tts("Aguarde enquanto os jogadores entram na sala")
            time.sleep(3)
            if self.button.start_game.text.lower() == 'start game':
                self.button.start_game.click()
                self.tts("O jogo começou!")
            else:
                self.tts("O jogo está a decorrer")
        except:
            self.tts("Não é permitido, começar o jogo neste momento")

    def leave_prison(self):
        print("Game : leave_prison")
        try:
            print(self.button.prison_pay.text.lower())
            if 'get free' in self.button.prison_pay.text.lower():
                self.button.prison_pay.click()
                self.tts("Pagaste para sair da prisão")
            else:
                self.tts("Não estás na prisão")
        except:
            self.tts("Não é permitido, sair da prisão neste momento")

    def give_up_game(self):
        print("Game : give_up_game")
        try: 
            self.button.bankrupt.click()
            time.sleep(1)
            self.tts("Tem a certeza que quer desistir do jogo?")
        except:
            self.tts("Não é permitido, desistir do jogo neste momento")

    def confirm_give_up_game(self):
        print("Game : confirm_give_up_game")
        try:
            self.button.confirm_bankrupt.click()
            self.tts("Desististe do jogo")
        except:
            self.tts("Não é permitido, desistir do jogo neste momento")

    def cancel_give_up_game(self):
        print("Game : cancel_give_up_game")
        try:
            self.button.cancel_bankrupt.click()
            self.tts("Ainda bem que não desististe")
        except:
            self.tts("Não é permitido, cancelar a desistência do jogo neste momento")

    def close(self):
        self.browser.close()
