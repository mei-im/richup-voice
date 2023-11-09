import time
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from mapping import Buttons, Inputs, Houses, Colors


class Game:
    def __init__(self) -> None:
        self.browser = Firefox()
        self.browser.get('https://richup.io/')
        self.browser.maximize_window()
        self.button = Buttons(self.browser)
        self.input = Inputs(self.browser)
        self.house = Houses(self.browser)
        self.colors = Colors(self.browser)
        time.sleep(2)
        self.button.accept_cookies.click()


    def join_game(self, name):
        self.input.name.send_keys(name)
        self.button.play.click()
        time.sleep(2)
        self.button.join_game.click()

    def list_house_information(self,house_name):
        house = self.house.__getattribute__(house_name)
        house.click()

    def choose_color(self, color):
        color = self.colors.__getattribute__(color)
        color.click()

    def roll_dice(self):
        # TODO : Check if the element is present
        text = self.button.roll_dice.text
        if text == 'Roll the dice':
            self.button.roll_dice.click()
        else:
            print('It\'s not your turn to roll the dice')
            # raise GameException('It\'s not your turn to roll the dice')

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

    def join_game_after_color(self):
        # TODO: ckeck if the element is present
        self.button.join_game_after_color.click()

    def start_game(self):
        self.button.start_game.click()


    def close(self):
        self.browser.close()
