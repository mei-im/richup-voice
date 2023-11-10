import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from mapping import Buttons, Inputs, Houses, Colors


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
        # TODO : DIZER QUE PODE INTERAGIR 


    # def join_game(self, name):
    #     self.input.name.send_keys(name)
    #     self.button.play.click()
    #     time.sleep(2)
    #     self.button.join_game.click()

    def list_house_information(self,house_name):
        house = self.house.__getattribute__(house_name)
        house.click()

    def choose_color(self, color):
        if self.button.join_game_after_color.text.lower() == 'join game':
            color = self.colors.__getattribute__(color)
            color.click()
            time.sleep(2)
            self.button.join_game_after_color.click()
        else:
            self.tts("You can't choose a color now")

    def roll_dice(self):
        # TODO : Check if the element is present
        if self.button.roll_dice.text.lower() == 'roll the dice' or \
            self.button.roll_dice.text.lower() == 'roll again':
            self.button.roll_dice.click()
        else:
            print('You can\'t roll the dice now')
            self.tts("Não podes lançar os dados agora")

    def end_turn(self):
        # TODO: ckeck if the element is present
        if self.button.end_turn.text == 'End turn':
            self.button.end_turn.click()
        else:
            print('It\'s not time to end the turn')
            # raise GameException('It\'s not time to end the turn')

    def buy(self):
        # TODO: ckeck if the element is present
        if "Buy" in self.button.buy.text:
            self.button.buy.click()
        else:
            print('You can\'t buy this house')
            # raise GameException('You can\'t buy this house')

    def start_game(self):
        if self.button.enable_bots:
            self.button.enable_bots.click()
        time.sleep(10)
        # TODO AVISAR QUE OS JOGADORES ESTAO A ENTRAR
        if self.button.start_game.text.lower() == 'start game':
            self.button.start_game.click()
        else:
            print('The game has already started')
            # raise GameException('The game has already started')

    def leave_prison(self):
        pass

    def give_up_game(self):
        pass


    def close(self):
        self.browser.close()
