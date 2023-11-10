import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from mapping import Buttons, Inputs, Houses, Colors
from new_dictonarys import colors_in_pt


class Game:
    def __init__(self, TTS) -> None:
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.button = Buttons(self.browser)
        self.input = Inputs(self.browser)
        self.house = Houses(self.browser)
        self.colors = Colors(self.browser)
        self.tts = TTS
        time.sleep(2)
        self.button.accept_cookies.click()
        time.sleep(1)
        self.tts("Para começar, insere o teu nome e inicia a sessão")

    # def join_game(self, name):
    #     self.input.name.send_keys(name)
    #     self.button.play.click()

    def create_game(self):
        self.button.create_game.click()
        self.tss("Escolha a cor com que quer jogar")

    def list_house_information(self,house_name):
        # TODO VOICE
        house = self.house.__getattribute__(house_name)
        house.click()

    def choose_color(self, color):
        if self.button.join_game_after_color.text.lower() == 'join game':
            color = self.colors.__getattribute__(color)
            color.click()
            name_color = colors_in_pt[color]
            self.tss(f"Ficaste com a cor {name_color}")
            time.sleep(2)
            self.tss("Espera que entre na sala")
            self.button.join_game_after_color.click()
            self.tss("Bem vindo ao sua sala")
        else:
            self.tts("You can't choose a color now")

    def roll_dice(self):
        # TODO : Check if the element is present
        if self.button.roll_dice.text.lower() == 'roll the dice' or \
            self.button.roll_dice.text.lower() == 'roll again':
            self.button.roll_dice.click()
        else:
            self.tts("Não podes lançar os dados agora")

    def end_turn(self):
        # TODO: ckeck if the element is present
        if self.button.end_turn.text == 'End turn':
            self.button.end_turn.click()
        else:
            self.tts("Não podes acabar a ronda agora")

    def buy(self):
        # TODO: ckeck if the element is present
        if "Buy" in self.button.buy.text:
            self.button.buy.click()
            self.tts("Adquiriste a propriedade")
        else:
            self.tts("Não podes comprar nenhuma propriedade por agora")

    def start_game(self):
        if self.button.enable_bots:
            self.button.enable_bots.click()
        self.tts("Aguarde enquanto os jogadores entram na sala")
        time.sleep(10)
        if self.button.start_game.text.lower() == 'start game':
            self.button.start_game.click()
            self.tts("O jogo começou")
        else:
            print("Error")

    def leave_prison(self):
        pass

    def give_up_game(self):
        pass


    def close(self):
        self.browser.close()
