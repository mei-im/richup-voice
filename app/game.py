import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from utils import *
from mapping import Buttons, Inputs, Houses, Colors
from new_dictonarys import colors_in_pt


class Game:
    def __init__(self, TTS) -> None:
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.mute = False
        self.tts_func = TTS
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

    def get_url(self):
        return self.browser.current_url
    
    def insert_name(self, name): # DONE
        try:
            if self.input.name.get_attribute("value") != "":
                self.input.name.clear()
            self.input.name.send_keys(name)
            self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
            time.sleep(3)
            self.tts("Se ainda não tens uma sala, podes criar uma sala para ti e para os teus amigos")
        except:
            self.tts(random_not_auth_insert_name())

    def create_game(self): # DONE
        try: 
            if self.button.create_private_game:
                if self.input.name.get_attribute("value") == "":
                    self.tts("Como não inseriste nenhum nome, vou criar um nome aleatório para ti")
                    self.button.randomize_name.click()
                    self.tts("O teu nome no jogo é " + self.input.name.get_attribute("value"))
                self.tts("A criar uma sala!")
                time.sleep(1)
                self.button.create_private_game.click()
                self.tts("Escolha a cor com que quer jogar")
            else:
                self.tts(random_not_create_room())
        except:
            self.tts(random_not_create_room())

    def list_house_information(self,house_name):

        if self.get_url() == "https://richup.io/":
            self.tts("Precisas de entrar numa sala para acessar ao tabuleiro do jogo")
            return
        
        house = self.house.__getattribute__(house_name)
        house.click()
        self.tts(f"Já consegues ver a informação da propriedade {house_name}")
        time.sleep(5)
        house.click()
        self.tts("A informação da propriedade foi minimizada")

    # DONE
    def choose_color(self, color):
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        
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
    
    def roll_dice(self):# DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try: 
            if self.button.roll_dice.text.lower() == 'roll the dice' or \
                self.button.roll_dice.text.lower() == 'roll again':
                self.button.roll_dice.click()
                self.tts(random_roll_dice())
            elif self.button.roll_dice.text.lower() == 'start game':
                self.tts("Precisa de começar o jogo para poder jogar")
            else:
                self.tts(random_roll_dice_in_turn())
        except: 
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_roll_dice_not_auth())
            except:
                self.tts(random_roll_dice_not_auth())
    
    def end_turn(self):# DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        
        try: 
            if self.button.end_turn.text == 'End turn':
                self.button.end_turn.click()
                self.tts(random_end_turn())
            elif self.button.roll_dice.text.lower() == 'start game':
                self.tts("Precisa de começar o jogo para poder jogar")
            else:
                self.tts(random_end_turn_not_auth())
        except:
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_end_turn_not_auth())
            except:
                self.tts(random_end_turn_other_player())

    def buy(self):# DONE

        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return

        try:
            if "Buy" in self.button.buy.text:
                self.button.buy.click()
                self.tts(random_buy_house())
            else:
                self.tts(random_buy_house_not_auth())
        except:
            try:
                if self.button.roll_dice.text.lower() == 'roll the dice' or \
                    self.button.roll_dice.text.lower() == 'roll again' or \
                    self.button.roll_dice.text.lower() == 'end turn':
                    self.tts(random_buy_house_not_auth())
                else:
                    self.tts(random_buy_house_not_in_game())
            except:
                self.tts(random_buy_house_not_in_game())

    def start_game(self):# DONE

        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try:
            if self.button.enable_bots:
                self.button.enable_bots.click()
            time.sleep(3)
            self.tts("Aguarde enquanto os jogadores entram na sala")
            time.sleep(3)
            if self.button.start_game.text.lower() == 'start game':
                self.button.start_game.click()
                self.tts(random_start_game())
        except:
            try:
                if self.button.join_game_after_color.text.lower() == 'join game':
                    self.tts("Precisa de entrar na sala para poder jogar")
                else:
                    self.tts(random_start_game_not_auth())
            except:
                self.tts(random_start_game_not_auth())

    def leave_prison(self):

        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        
        try:
            print(self.button.prison_pay.text.lower())
            if 'get free' in self.button.prison_pay.text.lower():
                self.button.prison_pay.click()
                self.tts("Pagaste para sair da prisão")
            else:
                self.tts("Não estás na prisão")
        except:
            self.tts("Não é permitido, sair da prisão neste momento")

    def give_up_game(self): # DONE
        if self.get_url() == "https://richup.io/":
            self.tts(random_create_room())
            return
        try: 
            self.button.bankrupt.click()
            time.sleep(1)
            self.tts("Tem a certeza que quer desistir do jogo?")
        except:
            self.tts(random_give_up_not_in_game())

    def confirm_give_up_game(self): # DONE
        print("confirm")
        try:
            self.button.confirm_bankrupt.click()
            self.tts(random_give_up_confirm())
        except:
            print("Not in game")
            self.tts(random_give_up_not_in_game())

    def cancel_give_up_game(self): # DONE
        try:
            self.button.cancel_bankrupt.click()
            self.tts(random_give_up_cancel())
        except:
            self.tts(random_give_up_not_in_game())

    def close(self): # DONE
        self.browser.close()

    def mute_func(self): #DONE
        def do_nothing(message):
            pass
        if self.mute:
            self.tts("O som já está desativado")
            return
        self.tts("O jogo vai ser silenciado, para voltar a ouvir o jogo, peça para sair do modo silencioso")
        self.button.mute.click()
        self.mute = True
        time.sleep(3)
        self.tts = do_nothing

    def unmute(self): #DONE
        if not self.mute:
            self.tts("O som não está desativado")
            return
        self.button.unmute.click()
        self.mute = False
        self.tts = self.tts_func
        time.sleep(3)
        self.tts("O jogo já não está silenciado")

    